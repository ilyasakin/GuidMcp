using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using GuidMcp.Tools;

using var host = new HostBuilder()
    .ConfigureServices(services =>
    {
        services.AddMcpServer()
            .WithStdioServerTransport()
            .WithTools<GuidTools>();
    })
    .Build();

await host.RunAsync();
