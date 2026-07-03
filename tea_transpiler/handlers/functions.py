"""
Handle Tea function definitions
"""

from ..patterns import FUNCTION


def handle_function(line):
    """
    Convert Tea function to Python function stub
    
    Example:
        tea.functions : fun greet(name)
        →
        def greet(name):
            pass  # add body
    """
    if 'tea.functions' not in line:
        return None
    
    match = FUNCTION.search(line)
    if not match:
        return None
    
    name = match.group(1).strip()
    args = match.group(2).strip()
    
    return f'def {name}({args}):\n    pass  # add body'
