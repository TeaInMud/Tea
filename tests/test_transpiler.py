"""
Tests for the Tea transpiler
"""

import os
from tea_transpiler import transpile


def load_fixture(filename):
    """Load a .tea fixture file from the fixtures folder"""
    path = os.path.join(os.path.dirname(__file__), 'fixtures', filename)
    with open(path, 'r') as f:
        return f.read()


def test_hello():
    """Test basic print statement"""
    code = load_fixture('hello.tea')
    result = transpile(code)
    assert 'print(' in result
    assert 'Hello' in result


def test_variables():
    """Test variable declarations"""
    code = load_fixture('variables.tea')
    result = transpile(code)
    assert 'x = 10' in result
    assert 'name = "Alice"' in result


def test_loops():
    """Test while and repeat loops"""
    code = load_fixture('loops.tea')
    result = transpile(code)
    assert 'while' in result
    assert 'for _ in range(' in result
