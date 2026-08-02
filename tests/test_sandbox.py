import pytest
import os
import tempfile
from mcp_sandbox.sandbox import Sandbox, SecurityException

def test_sandbox_read_write():
    with tempfile.TemporaryDirectory() as temp_dir:
        sandbox = Sandbox(temp_dir)
        
        sandbox.write_text("hello.txt", "world")
        assert sandbox.read_text("hello.txt") == "world"
        
        # Absolute path behavior (should treat as relative to sandbox root)
        sandbox.write_text("/abs_test.txt", "data")
        assert sandbox.read_text("abs_test.txt") == "data"
        assert sandbox.read_text("/abs_test.txt") == "data"

def test_sandbox_traversal():
    with tempfile.TemporaryDirectory() as temp_dir:
        sandbox = Sandbox(temp_dir)
        
        with pytest.raises(SecurityException):
            sandbox.read_text("../outside.txt")
            
        with pytest.raises(SecurityException):
            sandbox.write_text("../../etc/passwd", "hacked")

def test_sandbox_listdir_and_remove():
    with tempfile.TemporaryDirectory() as temp_dir:
        sandbox = Sandbox(temp_dir)
        
        sandbox.write_text("a.txt", "A")
        sandbox.write_text("b/c.txt", "C")
        
        files = sandbox.list_dir()
        assert "a.txt" in files
        assert "b" in files
        
        sandbox.remove("a.txt")
        files = sandbox.list_dir()
        assert "a.txt" not in files
