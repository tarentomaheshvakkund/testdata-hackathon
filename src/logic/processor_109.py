"""Code with deep nesting."""

def process(data):
    if data:
        if data.get('type') == 'user':
            if data.get('active'):
                if data.get('verified'):
                    if data.get('role') == 'admin':
                        if data.get('permissions'):
                            for p in data['permissions']:
                                if p.get('write'):
                                    return True
    return False
