"""
Tea Language Transpiler
Converts Tea source code to Python
"""

from .transpiler import transpile
from .compiler import compile_tea, run_tea

__version__ = "1.0.0"
__all__ = ["transpile", "compile_tea", "run_tea"]
