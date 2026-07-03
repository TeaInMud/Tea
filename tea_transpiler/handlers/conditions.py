"""
Handle Tea conditional statements
"""

from ..patterns import CONDITION


def handle_condition(line):
    """
    Convert Tea condition to Python if statement
    
    Example:
        tea.conditions : x > 5 { print "big" }  
        →  
        if x > 5:
            print("big")
    """
    if 'tea.conditions' not in line:
        return None
    
    match = CONDITION.search(line)
    if not match:
        return None
    
    condition = match.group(1).strip()
    body = match.group(2).strip()
    
    return f'if {condition}:\n    {body}'
