"""Problem Set 7: Regular, um, Expressions
https://cs50.harvard.edu/python/2022/psets/7/um/

It's not uncommon, in English, at least, to say “um” when trying to, um, think of a word.
The more you do it, though, the more noticeable it tends to be!

In a file called um.py, implement a function called count that expects a line of text as input as a
str and returns, as an int, the number of times that “um” appears in that text, case-insensitively,
as a word unto itself, not as a substring of some other word. For instance, given text like
"hello, um, world", the function should return 1. Given text like "yummy", though, the function
should return 0.

"""

import re


def main():
    print(count_ums(input("Text: ")))


def count_ums(s):
    """Return the number of "um"s (case insensitive and as stand-alone words) in a string.

    Parameters
    ----------
    s : str
        String to examine for "um"s.

    Returns
    -------
    int
        Count of the number of "um"s found in the string, s
    """

    ums = re.findall(r'\bum\b', s, flags=re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()