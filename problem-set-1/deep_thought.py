"""CS50P -- Problem Set 1: Deep Thought
Source: https://cs50.harvard.edu/python/2022/psets/1/deep/

In deep.py, implement a program that prompts the user for the answer to the Great
Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case
-insensitively) forty-two or forty two. Otherwise output No.
"""
acceptable_anwers = ['42', 'forty-two', 'forty two']
answer = input('What is the answer to the Great Question of Life, the Universe and Everything? ')

if answer.lower() in acceptable_anwers:
    print('Yes')
else:
    print('No')

# Longer solution
if answer == '42':
    print('Yes')
elif answer.lower() == 'forty-two':
    print('Yes')
elif answer.lower() == 'forty two':
    print('Yes')
else:
    print('No')