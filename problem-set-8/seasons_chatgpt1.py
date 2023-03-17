# From ChatGPT

import sys
from datetime import datetime, timedelta, date


def get_age_in_minutes(dob: date) -> int:
    now = datetime.now()
    dob = datetime.combine(dob, datetime.min.time())
    age_in_seconds = (now - dob).total_seconds()
    age_in_minutes = age_in_seconds / 60
    return round(age_in_minutes)


def convert_to_words(number: int) -> str:
    words = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
        "thirty",
        "thirty one",
        "thirty two",
        "thirty three",
        "thirty four",
        "thirty five",
        "thirty six",
        "thirty seven",
        "thirty eight",
        "thirty nine",
        "forty",
        "forty one",
        "forty two",
        "forty three",
        "forty four",
        "forty five",
        "forty six",
        "forty seven",
        "forty eight",
        "forty nine",
        "fifty",
        "fifty one",
        "fifty two",
        "fifty three",
        "fifty four",
        "fifty five",
        "fifty six",
        "fifty seven",
        "fifty eight",
        "fifty nine",
        "sixty",
        "sixty one",
        "sixty two",
        "sixty three",
        "sixty four",
        "sixty five",
        "sixty six",
        "sixty seven",
        "sixty eight",
        "sixty nine",
        "seventy",
        "seventy one",
        "seventy two",
        "seventy three",
        "seventy four",
        "seventy five",
        "seventy six",
        "seventy seven",
        "seventy eight",
        "seventy nine",
        "eighty",
        "eighty one",
        "eighty two",
        "eighty three",
        "eighty four",
        "eighty five",
        "eighty six",
        "eighty seven",
        "eighty eight",
        "eighty nine",
        "ninety",
        "ninety one",
        "ninety two",
        "ninety three",
        "ninety four",
        "ninety five",
        "ninety six",
        "ninety seven",
        "ninety eight",
        "ninety nine"
    ]
    if number < 100:
        return words[number]
    else:
        return "invalid number"


def convert_to_words_no_and(number: int) -> str:
    if number < 100:
        return convert_to_words(number)
    else:
        return "invalid number"


def get_date_from_input(input_str: str) -> date:
    try:
        return datetime.strptime(input_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid
