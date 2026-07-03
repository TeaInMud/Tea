#!/usr/bin/env python3
"""
Tea Language - CLI Entry Point
Usage: python tea.py [compile|run] <file.tea>
"""

import sys
import os
from tea_transpiler import compile_tea, run_tea


def print_usage():
    print("🍵 Tea Language v1.0")
    print("Usage: python tea.py [compile|run] <file.tea>")
    print()
    print("Commands:")
    print("  compile    Transpile .tea file to .py")
    print("  run        Compile and execute .tea file")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(0)

    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    file = sys.argv[-1]

    if cmd == "compile":
        compile_tea(file)
    elif cmd == "run":
        run_tea(file)
    else:
        print(f"Unknown command: {cmd}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
