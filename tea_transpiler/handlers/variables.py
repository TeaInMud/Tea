"""
Handle Tea variable declarations
"""

from ..patterns import VARIABLE
from ..utils import clean_quotes


def handle_variable(line):
    """
    Convert Tea variable to Python assignment
    
    Example:
        tea.variables : x is 10        →  x = 10
        tea.variables : name is "Bob"  →  name = "Bob"
    """
    if 'tea.variables' not in line:
        return None
    
    match = VARIABLE.search(line)
    if not match:
        return None
    
    name = match.group(1).strip()
    value = clean_quotes(match.group(2).strip())
    
    return f'{name} = {value}'
