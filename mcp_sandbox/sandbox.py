import os


class SecurityException(Exception):
    pass

class Sandbox:
    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)
            
    def _resolve_and_check(self, path: str) -> str:
        """Resolve path and ensure it's inside the sandbox root."""
        # If path is absolute, strip leading slash so it joins with root_dir
        if os.path.isabs(path):
            path = path.lstrip(os.sep)
            
        target = os.path.abspath(os.path.join(self.root_dir, path))
        
        if not target.startswith(self.root_dir):
            raise SecurityException(f"Path traversal detected! Attempted to access: {path}")
            
        return target
        
    def open(self, path: str, mode: str = 'r', encoding: str = 'utf-8'):
        target = self._resolve_and_check(path)
        
        # Ensure directory exists for writes
        if 'w' in mode or 'a' in mode:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            
        return open(target, mode, encoding=encoding)
        
    def read_text(self, path: str) -> str:
        with self.open(path, 'r') as f:
            return f.read()
            
    def write_text(self, path: str, content: str):
        with self.open(path, 'w') as f:
            f.write(content)
            
    def list_dir(self, path: str = "") -> list:
        target = self._resolve_and_check(path)
        if not os.path.exists(target):
            return []
        return os.listdir(target)
        
    def remove(self, path: str):
        target = self._resolve_and_check(path)
        if os.path.exists(target):
            if os.path.isdir(target):
                os.rmdir(target)
            else:
                os.remove(target)
