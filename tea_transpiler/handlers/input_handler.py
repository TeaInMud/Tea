"""
Handle Tea input statements
"""

from ..patterns import INPUT_WITH_VAR, INPUT_PLAIN
from ..utils import clean_quotes, strip_quotes


def handle_input(line):
    """
    Convert Tea input to Python input
    
    Examples:
        tea.system : input "Name: " >> name   →  name = input("Name: ")
        tea.system : input "Press enter..."    →  input("Press enter...")
    """
    if 'tea.system' not in line or 'input' not in line:
        return None
    
    # Input with variable assignment
    match = INPUT_WITH_VAR.search(line)
    if match:
        prompt = clean_quotes(match.group(1).strip())
        prompt = strip_quotes(prompt)
        var_name = match.group(2).strip()
        return f'{var_name} = input("""{prompt}""")'
    
    # Plain input (no variable)
    match = INPUT_PLAIN.search(line)
    if match:
        prompt = clean_quotes(match.group(1).strip())
        prompt = strip_quotes(prompt)
        return f'input("""{prompt}""")'
    
    return None
