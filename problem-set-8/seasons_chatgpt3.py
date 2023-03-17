# Third try from ChatGPT

import sys
from datetime import datetime, date


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format, please use YYYY-MM-DD")
        sys.exit(1)


def age_in_minutes(birthdate):
    now = datetime.now().date()
    age_in_seconds = (now - birthdate).total_seconds()
    age_in_minutes = round(age_in_seconds / 60)
    return age_in_minutes


def number_to_word(number):
    words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    }

    if number in words:
        return words[number]

    if number < 100:
        return f"{words[number//10*10]}-{words[number%10]}"

    if number < 1000:
        return f"{words[number//100]} hundred {'and ' + number_to_word(number%100) if number%100 > 0 else ''}"

    if number < 1_000_000:
        return f"{number_to_word(number//1000)} thousand {'and ' + number_to_word(number%1000) if number%1000 > 0 else ''}"


def age_in_words(birthdate):
    age_in_min = age_in_minutes(birthdate)
    return number_to_word(age_in_min)


def main():
    birthdate_str = input("Please enter your birthdate in YYYY-MM-DD format: ")
    birthdate = parse_date(birthdate_str)
    age_words = age_in_words(birthdate)
    print(f"You are {age_words} minutes old!")


if __name__ == "__main__":
    main()
