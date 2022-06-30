"""
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