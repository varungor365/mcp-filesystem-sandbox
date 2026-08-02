<div align="center">

# 🔒 mcp-filesystem-sandbox

**File system sandbox wrapper for Model Context Protocol (MCP) servers.**

[![PyPI version](https://badge.fury.io/py/mcp-filesystem-sandbox.svg)](https://badge.fury.io/py/mcp-filesystem-sandbox)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br/>

</div>

---

## ✨ Why this exists

If you're exposing local filesystem tools via the Model Context Protocol (MCP) to LLMs, you need to ensure the LLM doesn't accidentally (or maliciously) traverse your filesystem and read/write files it shouldn't.

`mcp-filesystem-sandbox` provides a strict, Python-native sandbox environment. It intercepts path traversals (like `../../etc/passwd`) and absolute path bypasses, guaranteeing all file operations stay within a designated root folder.

### Features
- 🛡️ **Path Traversal Protection:** Blocks all attempts to escape the root directory.
- 📁 **Transparent API:** Easy drop-in replacements for `open()`, `read()`, and `write()`.
- ⚡ **Zero Dependencies:** Pure Python, standard library only.

---

## 🚀 Quickstart

### Install
```bash
pip install mcp-filesystem-sandbox
```

### Usage

Wrap your MCP filesystem operations using the `Sandbox` class:

```python
from mcp_sandbox.sandbox import Sandbox, SecurityException

# Create a sandbox locked to a specific directory
sb = Sandbox("/path/to/my/workspace")

# Safe reads
data = sb.read_text("hello.txt")

# Safe writes (creates directories automatically)
sb.write_text("nested/folder/data.json", '{"key": "value"}')

# 🚫 Throws SecurityException!
try:
    sb.read_text("../../../../etc/passwd")
except SecurityException as e:
    print(f"Blocked malicious access: {e}")
```

---

## 🤖 AI Agent Context

See [CLAUDE.md](CLAUDE.md) for contribution guidelines.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.
