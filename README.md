# GuidMcp - GUID Generation MCP Server

A simple Model Context Protocol (MCP) server that provides GUID generation functionality for AI assistants and other MCP clients.

## Overview

This project implements an MCP server that exposes a single tool for generating GUIDs (Globally Unique Identifiers). The server uses the stdio transport protocol to communicate with MCP clients, making it easy to integrate with various AI assistants and development tools.

## Features

- **Generate GUID**: Creates a new random GUID in standard string format
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

The AI assistant will call the `GenerateGuid` tool and return a fresh GUID each time.

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