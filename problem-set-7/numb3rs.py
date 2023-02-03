"""Problem Set 7: NUMB3RS
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
    print(validate_ip(input("IPv4 Address: ")))


def validate_ip(ip):
    """Valiate an IP address based on IPv4 specs of a quad-dotted address with each
    component between 0 and 255.

    Parameters
    ----------
    ip : str
        An IP (internet protocol) address

    Returns
    -------
    bool
        True if valid, false if not
    """

    # Source for finding numbers in the range 000-255:
    # https://www.regextutorial.org/regex-for-numbers-and-ranges.php
    # [01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]
    valid_ip_num_range = r'([01]?\d\d?|2[0-4]\d|25[0-5])'
    pattern = '\.'.join([valid_ip_num_range] * 4)

    if re.match(pattern, ip):
        return True
    else:
        return False


def validate_ip_no_re(ip):
    """Valiate an IP address based on IPv4 specs of a quad-dotted address with each
    component between 0 and 255.

    This version does not use regular expressions to validate the address.

    Parameters
    ----------
    ip : str
        An IP (internet protocol) address

    Returns
    -------
    bool
        True if valid, false if not
    """

    # All IP addresses need to have a period in it...
    if not '.' in ip:
        return False

    else:
        nums = ip.split('.')

        # They also need to contain 4 numbers beteween 3 periods...
        if not len(nums) == 4:
            return False

        else:
            for num in nums:
                # Each num has to be a digit...
                if not num.isdigit():
                    return False

                # And each num has to be between 0 and 255
                if not 0 <= int(num) <= 255:
                    return False

    return True


if __name__ == "__main__":
    main()