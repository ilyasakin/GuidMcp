using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using GuidMcp.Tools;

var host = Host.CreateDefaultBuilder(args)
    .ConfigureServices(services =>
    {
        services.AddMcpServer()
            .WithStdioServerTransport()
            .WithTools<GuidTools>();
    })
    .Build();

await host.RunAsync();
