# GuidMcp - GUID Generation MCP Server

A simple Model Context Protocol (MCP) server that provides GUID generation functionality for AI assistants and other MCP clients.

## Overview

This project implements an MCP server that exposes tools for generating GUIDs (Globally Unique Identifiers). The server uses the stdio transport protocol to communicate with MCP clients, making it easy to integrate with various AI assistants and development tools.

## Features

- **Generate GUID**: Creates a new random GUID in standard string format
- **Generate Multiple GUIDs**: Creates multiple GUIDs in a single call for improved efficiency
- **Lightweight**: Minimal dependencies and fast startup time
- **Cross-platform**: Runs on Windows, macOS, and Linux
- **Standards-compliant**: Uses the standard .NET `Guid.NewGuid()` implementation

## Prerequisites

- .NET 8.0 or later
- An MCP-compatible client (such as Claude Desktop, Cursor, or other AI assistants)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ilyasakin/GuidMcp
   cd GuidMcp
   ```

2. Build the project:

   ```bash
   dotnet build
   ```

3. Run the server:
   ```bash
   dotnet run
   ```

## Usage

### Running the Server

The server communicates via standard input/output (stdio), so it's typically launched by an MCP client rather than run directly by users.

```bash
dotnet run
```

### Available Tools

#### GenerateGuid

Generates a new GUID and returns it as a string.

**Parameters**: None

**Returns**: A string representation of a newly generated GUID

**Example output**:

```
a6af25e4-649f-47cb-9ed8-0a5ca26d14e3
```

#### GenerateMultipleGuids

Generates multiple GUIDs and returns them as an array.

**Parameters**:

- `count` (int): The number of GUIDs to generate

**Returns**: An array of strings, each containing a newly generated GUID

**Example output**:

```
[
  "a6af25e4-649f-47cb-9ed8-0a5ca26d14e3",
  "b7f3d9e1-7a2b-4c5d-8e9f-1a2b3c4d5e6f",
  "c8g4e0f2-8b3c-5d6e-9f0g-2b3c4d5e6f7g"
]
```

### Integration with MCP Clients

To use this server with an MCP client, you'll need to configure the client to launch this server. Here's an example configuration:

```json
{
  "mcpServers": {
    "guid-generator": {
      "command": "dotnet",
      "args": ["run", "--project", "/path/to/GuidMcp"]
    }
  }
}
```

## Example Usage in AI Assistants

Once configured, you can ask your AI assistant to generate GUIDs:

- "Generate a new GUID for me"
- "I need a unique identifier"
- "Create a GUID for this new record"
- "Generate 5 GUIDs for my database records"
- "I need 10 unique identifiers"

The AI assistant will call the appropriate tool (`generate_guid` for single GUIDs or `generate_multiple_guids` for multiple GUIDs) and return fresh GUIDs each time.

## Development

### Project Structure

```
GuidMcp/
├── Program.cs              # Main entry point and server configuration
├── Tools/
│   └── GuidTools.cs       # GUID generation tool implementation
├── GuidMcp.csproj         # Project file
└── README.md              # This file
```

### Building and Testing

```bash
# Build the project
dotnet build

# Run the project
dotnet run

# Build for release
dotnet build --configuration Release
```

## LICENSE

MIT License

Copyright (c) 2025 ilyas akın

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
