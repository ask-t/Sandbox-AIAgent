#!/bin/bash
set -e

MCP_CONFIG=$(cat << 'EOF'
{
  "mcpServers": {
    "workspace": {
      "command": "uvx",
      "args": [
        "workspace-mcp",
        "--tool-tier",
        "complete"
      ],
      "env": {
        "GOOGLE_OAUTH_CLIENT_ID": "${GOOGLE_OAUTH_CLIENT_ID}",
        "GOOGLE_OAUTH_CLIENT_SECRET": "${GOOGLE_OAUTH_CLIENT_SECRET}",
        "OAUTHLIB_INSECURE_TRANSPORT": "1"
      }
    }
  }
}
EOF
)

# Gemini CLI
mkdir -p ~/.gemini
echo "$MCP_CONFIG" > ~/.gemini/settings.json

# Claude Code
mkdir -p ~/.claude
echo "$MCP_CONFIG" > ~/.claude/settings.json

echo "MCP configuration written."
