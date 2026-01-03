"""File reader with path traversal vulnerability."""
import os

def read_file(user_dir, filename):
    """Read file - VULNERABLE to path traversal."""
    filepath = os.path.join(user_dir, filename)
    with open(filepath, 'r') as f:
        return f.read()
