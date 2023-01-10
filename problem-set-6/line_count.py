"""CS50P -- Problem Set 6: Line Count
Source: https://cs50.harvard.edu/python/2022/psets/6/line/

In a file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines.

If the user does not specify exactly one command-line argument, or if the specified file's
name does not end in .py, or if the specified file does not exist, the program should instead
exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank.
"""
import sys

try:
    py_script = sys.argv[1]
except:
    sys.exit()
else:
    if not py_script.endswith('.py'):
        sys.exit('Sorry, we are expecting a python program as an argument. Please try again.')

line_count = 0

# Test comment
with open(py_script) as file:
    for line in file:
        if not (line.lstrip().startswith('#') or line == '\n'):
            line_count += 1

print(line_count)