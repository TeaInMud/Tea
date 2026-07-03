"""
Handle Tea imports: tea.import : something
"""

from ..patterns import IMPORT


def handle_import(line):
    """
    Convert Tea import to Python import
    
    Example:
        tea.import : import math    →  import math
        tea.import : from os import path  →  from os import path
    """
    match = IMPORT.search(line)
    if match:
        return match.group(1).strip()
    return None
