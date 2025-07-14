using ModelContextProtocol;
using ModelContextProtocol.Server;
using System.ComponentModel;
using System.Globalization;
using System.Text.Json;

namespace GuidMcp.Tools;

[McpServerToolType]
public sealed class GuidTools
{
    [McpServerTool, Description("Generate a new GUID.")]
    public static string GenerateGuid()
    {
        return Guid.NewGuid().ToString();
    }
}
