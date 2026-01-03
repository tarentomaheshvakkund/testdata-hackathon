"""Handler with bare except."""

def handle(request):
    try:
        return process(request)
    except:  # BAD: Catches everything
        return None
