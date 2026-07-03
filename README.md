# 🍵 Tea

A warm, beginner-friendly programming language that transpiles to Python.

## ✨ Why Tea?

No cryptic symbols. No intimidating syntax. Just readable code that feels like English.



## 🚀 Quick Start

```bash
# Run a Tea program
python tea.py run hello.tea

# Compile to Python
python tea.py compile hello.tea
```

📖 Example

```tea
< Greeting Program >
tea.system : input "What's your name? " >> name
tea.system : print "Hello, {name}!"
```

📦 Requirements

· Python 3.6+

📁 Project Structure

```
tea/
├── tea.py
├── tea_transpiler/
│   ├── transpiler.py
│   ├── compiler.py
│   ├── patterns.py
│   ├── utils.py
│   └── handlers/
│       ├── comments.py
│       ├── imports.py
│       ├── print_handler.py
│       ├── input_handler.py
│       ├── variables.py
│       ├── conditions.py
│       ├── loops.py
│       └── functions.py
├── examples/
└── README.md
```

📝 License

Proprietary. All rights reserved. See LICENSE.


Write like you speak. Run like Python. 🍵
