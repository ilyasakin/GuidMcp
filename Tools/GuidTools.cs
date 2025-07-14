using ModelContextProtocol.Server;
using System.ComponentModel;
using System;

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
