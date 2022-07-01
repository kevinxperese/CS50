"""CS50P -- Problem Set 0: Indoor Voice

Source: https://cs50.harvard.edu/python/2022/psets/0/indoor/
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then
outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged.
You're welcome, but not required, to prompt the user explicitly, as by passing a str of your own as
an argument to input.

"""

response = input("Type something in ALL CAPS, and I'll convert it to an 'indoor voice' version for you! ")
print(response.lower())
