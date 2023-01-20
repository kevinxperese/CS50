""" Problem Set 7: NUMB3RS
Source: https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on
the internet, akin to a postal address in the real world, typically formatted in dot-decimal
notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say
275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as
input as a str and then returns True or False, respectively, if that input is a valid IPv4 address
or not.
"""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Source for first capture group: https://www.regextutorial.org/regex-for-numbers-and-ranges.php
    pattern = re.compile(r'([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])(.\1){3}')

    if pattern.match(ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()