"""Problem Set 8: Seasons of Love
Source: https://cs50.harvard.edu/python/2022/psets/8/seasons/
"""

from datetime import date
import re
import sys


def main():
    input_bday = input("Enter your date of birth (in ISO-8601 format, please!): ")

    if not valid_date(input_bday):
        sys.exit("Invalid date. Please enter your birthday in ISO-8601 format!")

    mins_since_bday = calc_mins_since_bday(date.today(), input_bday)
    mins_since_bday_text = convert_num_to_text(mins_since_bday)

    print(f"{mins_since_bday_text} minutes")


def valid_date(_date):
    """Validate that a date string is in ISO-8601 format.
    Note: Don't need to check for month and day values being valid, because
    when the conversion to a datetime object is done, a ValueError will be thrown
    for months > 12 and day values that don't match the appropriate month.

    Parameters
    ----------
    _date : str
        Input string, hopefully containing a birthdate in ISO-8601 format.

    Returns
    -------
    bool
    """
    if re.match(r"\d{4}-\d{2}-\d{2}", _date):
        return True
    else:
        return False


def calc_mins_since_bday(today, input_bday):
    """Calculate number of minutes since birthday.
    Assume births occur at 0:00.00 and don't count minutes in today.

    Parameters
    ----------
    today : date
        Today's date, as a date object
    input_bday : str
        Birthday date, in ISO-8601 date format.

    Returns
    -------
    str
    """

    bday_ymd = [int(x) for x in input_bday.split('-')]
    time_delta = today - date(*bday_ymd)

    return str(int(time_delta.total_seconds() / 60))  # Don't want the trailing x.0s


def convert_num_to_text(num):
    """Convert a numeric string to a written out string of that number.

    Parameters
    ----------
    num : str
        String containing an integer.

    Returns
    -------
    str
    """

    ones = {
        '0' : 'zero',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine'
    }

    teens = {
        '10' : 'ten',
        '11' : 'eleven',
        '12' : 'twelve',
        '13' : 'thirteen',
        '14' : 'fourteen',
        '15' : 'fifteen',
        '16' : 'sixteen',
        '17' : 'seventeen',
        '18' : 'eighteen',
        '19' : 'nineteen'
    }

    tens = {
        '2' : 'twenty',
        '3' : 'thirty',
        '4' : 'forty',
        '5' : 'fifty',
        '6' : 'sixty',
        '7' : 'seventy',
        '8' : 'eighty',
        '9' : 'ninety'
    }


    if len(num) == 1:
        return ones[num]

    elif len(num) == 2:
        if num[0] == '0':
            return ones[num[1]]
        elif num[0] == '1':
            return teens[num]
        elif num[1] == '0':
            return tens[num[0]]
        else:
            return tens[num[0]] + '-' + ones[num[1]]

    elif len(num) == 3:
        if num[0] == '0':
            return convert_num_to_text(num[1:])
        elif num[1:] == '00':
            return ones[num[0]] + ' hundred'
        else:
            return ones[num[0]] + ' hundred ' + convert_num_to_text(num[1:])

    elif len(num) in [4, 5, 6]:
        if num[0] == '0':
            return convert_num_to_text(num[1:])
        elif num[-3:] == '000':
            return convert_num_to_text(num[:-3]) + ' thousand'
        else:
            return convert_num_to_text(num[:-3]) + ' thousand, ' + convert_num_to_text(num[-3:])

    elif len(num) in [7, 8, 9]:
        if num[0] == '0':
            return convert_num_to_text(num[1:])
        elif num[-6:] == '000000':
            return convert_num_to_text(num[:-6]) + ' million'
        else:
            return convert_num_to_text(num[:-6]) + ' million, ' + convert_num_to_text(num[-6:])


if __name__ == "__main__":
    main()
