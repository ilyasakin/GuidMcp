using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using GuidMcp.Tools;

using var host = Host.CreateDefaultBuilder(args)
    .ConfigureLogging(logging =>
    {
        // stdout is exclusively the MCP JSON-RPC transport.
        logging.AddConsole(options => options.LogToStandardErrorThreshold = LogLevel.Trace);
    })
    .ConfigureServices(services =>
    {
        services.AddMcpServer()
            .WithStdioServerTransport()
            .WithTools<GuidTools>();
    })
    .Build();

await host.RunAsync();
