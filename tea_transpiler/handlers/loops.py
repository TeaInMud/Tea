"""
Handle Tea loop constructs
"""

from ..patterns import WHILE_LOOP, REPEAT


def handle_while(line):
    """
    Convert Tea while loop to Python while loop
    
    Example:
        tea.loop while x < 5 { print x }
        →
        while x < 5:
            print(x)
    """
    if 'tea.loop while' not in line:
        return None
    
    match = WHILE_LOOP.search(line)
    if not match:
        return None
    
    condition = match.group(1).strip()
    body = match.group(2).strip()
    
    return f'while {condition}:\n    {body}'


def handle_repeat(line):
    """
    Convert Tea repeat to Python for loop
    
    Example:
        repeat 5 print "Hello"
        →
        for _ in range(5):
            print("Hello")
    """
    if not line.startswith('repeat '):
        return None
    
    match = REPEAT.search(line)
    if not match:
        return None
    
    count = match.group(1)
    action = match.group(2).strip() or 'pass'
    
    return f'for _ in range({count}):\n    {action}'
