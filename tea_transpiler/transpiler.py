"""
Main transpiler - orchestrates line-by-line conversion
"""

from .handlers.comments import handle_comment
from .handlers.imports import handle_import
from .handlers.print_handler import handle_print
from .handlers.input_handler import handle_input
from .handlers.variables import handle_variable
from .handlers.conditions import handle_condition
from .handlers.loops import handle_while, handle_repeat
from .handlers.functions import handle_function


# Ordered list of handlers - first match wins
HANDLERS = [
    handle_comment,
    handle_import,
    handle_print,
    handle_input,
    handle_variable,
    handle_condition,
    handle_while,
    handle_repeat,
    handle_function,
]


def transpile(tea_code):
    """
    Convert Tea source code to Python
    
    Args:
        tea_code: String containing Tea language code
        
    Returns:
        String containing equivalent Python code
    """
    output_lines = ["# Tea → Python"]
    
    for line in tea_code.split("\n"):
        stripped = line.strip()
        
        # Preserve empty lines
        if not stripped:
            output_lines.append("")
            continue
        
        # Try each handler
        handled = False
        for handler in HANDLERS:
            result = handler(stripped)
            if result is not None:
                output_lines.append(result)
                handled = True
                break
        
        # If no handler matched, pass through as-is
        if not handled:
            output_lines.append(stripped)
    
    return "\n".join(output_lines)
