# Fourth try from ChatGPT

import sys
from datetime import date, datetime


def calculate_age_in_minutes(birthdate):
    today = date.today()
    age_in_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_in_minutes = age_in_years * 365 * 24 * 60
    return age_in_minutes


def spell_out_number(number):
    words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    if number in words:
        return words[number]
    else:
        return words[number // 10 * 10] + "-" + words[number % 10]


def spell_out_minutes(minutes):
    if minutes == 0:
        return "zero minutes"
    elif minutes < 0:
        return "not born yet"
    else:
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)

        parts = []
        if years > 0:
            parts.append(spell_out_number(years) + " year" + ("s" if years > 1 else ""))
        if days > 0:
            parts.append(spell_out_number(days) + " day" + ("s" if days > 1 else ""))
        if hours > 0:
            parts.append(spell_out_number(hours) + " hour" + ("s" if hours > 1 else ""))
        if minutes > 0:
            parts.append(spell_out_number(minutes) + " minute" + ("s" if minutes > 1 else ""))

        return " ".join(parts)


def main():
    while True:
        try:
            birthdate_str = input("Enter your date of birth (YYYY-MM-DD): ")
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    age_in_minutes = calculate_age_in_minutes(birthdate)
    age_in_minutes_rounded = round(age_in_minutes)

    age_in_words = spell_out_minutes(age_in_minutes_rounded)

    print(f"You are {age_in_words} old.")


if __name__ == "__main__":
    main()
