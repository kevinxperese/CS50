"""CS50P -- Problem Set 0: Playback Speed

Source: https://cs50.harvard.edu/python/2022/psets/0/indoor/

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like
:( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and
returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face)
and any :( converted to 🙁 (otherwise known as a slightly frowning face).
All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls
convert on that input, and prints the result. You’re welcome, but not required, to prompt the user
explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the
bottom of your file.

"""

def main():
    response = input("How are you feeling today? ")
    response = response.replace(':)', convert(':)'))
    response = response.replace(':(', convert(':('))
    print(convert(response))
    return None

def convert(s):
    """Convert smile face or frowning face emoticons to emoji"""
    if s == ':)':
        # return "\U0001f600"
        return "🙂"
    elif s == ':(':
        # return "\U0001F641"
        return "🙁"
    else:
        return s

main()
