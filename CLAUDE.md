# mcp-filesystem-sandbox - AI Agent Guidelines

## Agent Context
If a user asks you to add new features to this sandbox:
1. Prioritize security over convenience. If a path resolves outside the root, block it.
2. Keep dependencies minimal. This should ideally remain zero-dependency (other than pytest for dev) so it can be easily embedded in any MCP server.
