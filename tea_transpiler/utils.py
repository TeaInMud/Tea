"""
Shared utilities for the transpiler
"""

import re


def clean_quotes(text):
    """Convert smart quotes to straight quotes"""
    return text.replace('\u201c', '"').replace('\u201d', '"')


def strip_quotes(text):
    """Remove surrounding quotes from a string"""
    text = text.strip()
    if (text.startswith('"') and text.endswith('"')) or \
       (text.startswith("'") and text.endswith("'")):
        return text[1:-1]
    return text


def is_quoted(text):
    """Check if text is wrapped in quotes"""
    text = text.strip()
    return (text.startswith('"') and text.endswith('"')) or \
           (text.startswith("'") and text.endswith("'"))


def has_interpolation(text):
    """Check if text contains f-string style interpolation"""
    return '{' in text and '}' in text
