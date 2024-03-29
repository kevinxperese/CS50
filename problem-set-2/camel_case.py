"""CS50P -- Problem Set 2: Camel Case
Source: https://cs50.harvard.edu/python/2022/psets/2/camel/

In some languages, it's common to use camel case (otherwise known as “mixed case”) for variables'
names when those names comprise multiple words, whereby the first letter of the first word is
lowercase but the first letter first letter of each subsequent word is uppercase.

For instance, whereas a variable for a user's name might be called name, a variable for a user's
first name might be called firstName, and a variable for a user's preferred first name
(e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_),
with all letters in lowercase. For instance, those same variables would be called name,
first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in
camel case and outputs the corresponding name in snake case.

Assume that the user's input will indeed be in camel case.
"""

camelCase = input("Enter a variable in camelCase format: ")

# First convert first letter to lower case
snake_case = camelCase[0].lower()

# Then loop over the remanining letters
for letter in camelCase[1:]:
    if letter.islower():
        snake_case += letter
    elif letter.isupper():
        snake_case += '_'
        snake_case += letter.lower()

print(snake_case)