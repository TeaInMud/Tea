"""
Regex patterns for parsing Tea language constructs
"""

import re

# tea.import : statement
IMPORT = re.compile(r'tea\.import\s*:\s*(.+)')

# tea.system : print ...
PRINT = re.compile(r'print\s+(.+)')

# tea.system : input "prompt" >> variable
INPUT_WITH_VAR = re.compile(r'input\s+(.+?)\s*>>\s*(.+)')

# tea.system : input "prompt"
INPUT_PLAIN = re.compile(r'input\s+(.+)')

# tea.variables : name is value
VARIABLE = re.compile(r':\s*(.+?)\s+is\s+(.+)')

# tea.conditions : condition { body }
CONDITION = re.compile(r':\s*(.+?)\s*\{(.+)\}')

# tea.loop while condition { body }
WHILE_LOOP = re.compile(r'while\s+(.+?)\s*\{(.+)\}')

# repeat N
REPEAT = re.compile(r'repeat\s+(\d+)\s*(.*)')

# tea.functions : fun name(args)
FUNCTION = re.compile(r'fun\s+(.+?)\((.*?)\)')
