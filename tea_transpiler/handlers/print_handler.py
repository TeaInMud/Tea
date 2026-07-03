"""
Handle Tea print statements
"""

from ..patterns import PRINT
from ..utils import clean_quotes, strip_quotes, is_quoted, has_interpolation


def handle_print(line):
    """
    Convert Tea print to Python print
    
    Examples:
        tea.system : print "Hello"        →  print("Hello")
        tea.system : print "Hi {name}"    →  print(f"Hi {name}")
        tea.system : print variable       →  print(variable)
    """
    if 'tea.system' not in line or 'print' not in line:
        return None
    
    match = PRINT.search(line)
    if not match:
        return None
    
    content = clean_quotes(match.group(1).strip())
    
    # f-string (has variable interpolation)
    if has_interpolation(content):
        if is_quoted(content):
            content = strip_quotes(content)
        return f'print(f"""{content}""")'
    
    # Variable or expression (no quotes)
    if not is_quoted(content):
        return f'print({content})'
    
    # Plain string
    text = strip_quotes(content)
    return f'print("""{text}""")'
