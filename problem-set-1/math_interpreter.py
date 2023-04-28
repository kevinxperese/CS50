"""CS50P -- Problem Set 1: Math Interpreter
Source: https://cs50.harvard.edu/python/2022/psets/1/interpreter

Python already supports math, whereby you can write code to add, subtract, multiply, or divide
values and even variables. But let's write a program that enables users to do math, even without
knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic
expression and then calculates and outputs the result as a floating-point value formatted to
one decimal place. Assume that the user's input will be formatted as x y z, with one space between
x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0.
Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py
be an interpreter for math!
"""
# Get equation components
x, y, z = input('Type an equation: ').split()

# Convert operands to integers
x_int = int(x)
z_int = int(z)

# Write out results, with appropriate formats
if y == '+':
    print(f"{x_int + z_int :.1f}")
elif y == '-':
    print(f"{x_int - z_int :.1f}")
elif y == '*':
    print(f"{x_int * z_int :.1f}")
elif y == '/':
    print(f"{x_int / z_int :.1f}")
