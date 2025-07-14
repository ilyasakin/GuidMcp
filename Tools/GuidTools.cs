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

    [McpServerTool, Description("Generate multiple GUIDs.")]
    public static string[] GenerateMultipleGuids(int count)
    {
        var guids = new string[count];
        for (int i = 0; i < count; i++)
        {
            guids[i] = Guid.NewGuid().ToString();
        }
        return guids;
    }
}
