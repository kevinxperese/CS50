"""CS50P -- Problem Set 2: Vanity Plates
Source: https://cs50.harvard.edu/python/2022/psets/2/plates/

In Massachusetts, home to Harvard University, it's possible to request a vanity
license plate for your car, with your choice of letters and numbers instead of 
random ones. Among the requirements, though, are:

* All vanity plates must start with at least two letters.
* … vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
* Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
    The first number used cannot be a '0'.
* No periods, spaces, or punctuation marks are allowed.

In plates.py, implement a program that prompts the user for a vanity plate and
then output "Valid" if meets all of the requirements or "Invalid" if it does not.

Assume that any letters in the user's input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets
all requirements and False if it does not. Assume that s will be a str.

You're welcome to implement additional functions for is_valid to call
(e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        is_right_length(s) and
        starts_with_two_letters(s) and
        ends_with_numeric(s) and
        first_number_not_zero(s) and
        has_no_punctuation(s)
    )


def is_right_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[0:2].isalpha()


def has_no_punctuation(s):
    # Note: Catches punctuation marks AND whitespace
    return s.isalnum()


def ends_with_numeric(s):
    for i, char in enumerate(s):
        if char.isnumeric():
            return s[i:].isnumeric()


def first_number_not_zero(s):
    for char in s:
        if char.isnumeric():
            return not char == '0'

main()
