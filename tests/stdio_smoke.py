"""Dependency-free MCP stdio regression test. Run against a built server."""
import json
import queue
import subprocess
import sys
import threading
import uuid


def read_lines(stream, output):
    for line in stream:
        output.put(line)
    output.put(None)


def main(command):
    if not command:
        raise SystemExit('Usage: python3 tests/stdio_smoke.py <server command> [args...]')
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, encoding='utf-8')
    lines = queue.Queue()
    errors = []
    threading.Thread(target=read_lines, args=(process.stdout, lines), daemon=True).start()
    threading.Thread(target=lambda: errors.extend(process.stderr), daemon=True).start()
    request_id = 0

    def send(message):
        process.stdin.write(json.dumps({'jsonrpc': '2.0', **message}) + '\n')
        process.stdin.flush()

    def request(method, params):
        nonlocal request_id
        request_id += 1
        send({'id': request_id, 'method': method, 'params': params})
        # Fail on logs/non-JSON stdout, and put a bound on a silent server.
        import time
        deadline = time.monotonic() + 20
        while True:
            line = lines.get(timeout=max(0, deadline - time.monotonic()))
            assert line is not None, 'Server exited: ' + ''.join(errors)
            message = json.loads(line)
            assert message.get('jsonrpc') == '2.0', message
            if message.get('id') == request_id:
                assert 'error' not in message, message
                return message['result']

    def call(name, arguments):
        return request('tools/call', {'name': name, 'arguments': arguments})

    def check_guids(result, count):
        assert not result.get('isError'), result
        content = result['content']
        assert len(content) == count, result
        values = []
        for block in content:
            assert block['type'] == 'text', block
            value = block['text']
            parsed = uuid.UUID(value)
            assert str(parsed) == value and parsed.version == 4, value
            values.append(value)
        assert len(set(values)) == count, values
        return values

    try:
        initialized = request('initialize', {
            'protocolVersion': '2025-03-26', 'capabilities': {},
            'clientInfo': {'name': 'guid-regression-test', 'version': '1.0.0'}})
        assert initialized['protocolVersion'] == '2025-03-26', initialized
        send({'method': 'notifications/initialized'})
        tools = request('tools/list', {})['tools']
        by_name = {tool['name']: tool for tool in tools}
        assert set(by_name) == {'generate_guid', 'generate_multiple_guids'}, by_name
        assert by_name['generate_guid']['description'] == 'Generate a new GUID.'
        multiple = by_name['generate_multiple_guids']
        assert multiple['description'] == 'Generate multiple GUIDs.'
        assert multiple['inputSchema']['properties']['count']['type'] == 'integer'
        assert multiple['inputSchema']['required'] == ['count']
        first = check_guids(call('generate_guid', {}), 1)
        second = check_guids(call('generate_guid', {}), 1)
        assert first != second
        for count in (0, 1, 5, 100):
            check_guids(call('generate_multiple_guids', {'count': count}), count)
        assert call('generate_multiple_guids', {'count': -1}).get('isError') is True
        # Invalid input must not kill the server or contaminate subsequent calls.
        check_guids(call('generate_guid', {}), 1)
        process.stdin.close()
        assert process.wait(timeout=10) == 0, ''.join(errors)
        while True:
            line = lines.get(timeout=5)
            if line is None:
                break
            assert json.loads(line).get('jsonrpc') == '2.0', line
        print('PASS: initialization, tool schema, GUID format/uniqueness, counts, error recovery, clean stdio and shutdown')
    finally:
        if process.poll() is None:
            process.kill()
            process.wait(timeout=10)


if __name__ == '__main__':
    main(sys.argv[1:])
