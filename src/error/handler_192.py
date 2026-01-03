"""Empty catch blocks."""

def process(filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except:
        pass  # Silent failure
