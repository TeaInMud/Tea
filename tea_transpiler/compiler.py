"""
File operations for Tea compilation
"""

import os
from .transpiler import transpile


def compile_tea(source_file):
    """
    Compile a .tea file to .py
    
    Args:
        source_file: Path to .tea source file
        
    Returns:
        Path to generated .py file, or None on error
    """
    if not source_file.endswith('.tea'):
        print("Error: File must have .tea extension")
        return None
    
    if not os.path.exists(source_file):
        print(f"Error: File not found: {source_file}")
        return None
    
    py_file = source_file.replace('.tea', '.py')
    
    with open(source_file, 'r', encoding='utf-8') as f:
        tea_code = f.read()
    
    py_code = transpile(tea_code)
    
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(py_code)
    
    print(f"✅ Compiled: {source_file} → {py_file}")
    return py_file


def run_tea(file_path):
    """
    Compile and run a .tea file, or run a .py file directly
    
    Args:
        file_path: Path to .tea or .py file
    """
    if file_path.endswith('.tea'):
        py_file = compile_tea(file_path)
    else:
        py_file = file_path
    
    if py_file and os.path.exists(py_file):
        print(f"▶ Running: {py_file}")
        print("─" * 40)
        
        with open(py_file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        try:
            exec(code)
        except Exception as e:
            print(f"❌ Runtime error: {e}")
        
        print("─" * 40)
