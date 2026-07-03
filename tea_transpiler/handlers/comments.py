"""
Handle Tea comments: < This is a comment >
"""

def handle_comment(line):
    """
    Convert Tea comments to Python comments
    
    Example:
        < Hello World >  →  # Hello World
    """
    if line.startswith('<') and line.endswith('>'):
        return '# ' + line[1:-1].strip()
    return None
