"""CS50P -- Problem Set 2: Just setting up my twttr
Source: https://cs50.harvard.edu/python/2022/psets/2/twttr/

When texting or tweeting, it's not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr.

In a file called twttr.py, implement a program that prompts the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in
uppercase or lowercase.
"""

user_text = input('Input: ')

no_vowels = ''
for char in user_text:
    if not char.lower() in ['a', 'e', 'i', 'o', 'u']:
        no_vowels += char

print(no_vowels)
