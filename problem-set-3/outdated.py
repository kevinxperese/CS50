"""CS50P -- Problem Set 3: Outdated
Source: https://cs50.harvard.edu/python/2022/psets/3/outdated/

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise
known as middle-endian order, which is arguably bad design.

Dates in that format can't be easily sorted because the date's year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program
(e.g., a spreadsheet).

Dates in that format are also ambiguous.
Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates
should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years
with four digits, months with two digits, and days with two digits, “padding” each with leading
zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in
month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter
might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user's input is not a valid date in either
format, prompt the user again.

Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def check_date(year: str, month: str, day: str) -> bool:

    good_day = (
        day.isdigit() and
        1 <= len(day) <= 2 and
        1 <= int(day) <= 31
    )

    good_month = (
        month.isdigit() and
        1 <= len(month) <= 2 and
        1 <= int(month) <= 12
    )

    good_year = (
        year.isdigit() and
        len(year) == 4
    )

    return (
        good_day and
        good_month and
        good_year
    )


while True:
    date = input('Date: ')

    if '/' in date:
        try:
            month, day, year = date.split('/')
            month, day = month.zfill(2), day.zfill(2)
        except ValueError:
            # Will occur if there aren't *exactly* 2 '/'s in date
            continue

    elif ' ' in date:
        try:
            month, day, year = date.split(' ')
            month = str(months.index(month) + 1).zfill(2)
            day = day.rstrip(',').zfill(2)
        except ValueError:
            # Will occur if there aren't *exactly* 2 spaces in date OR if month isn't in months
            continue

    else:  # date doesn't contain either '/' or ' ', so prompt again
        continue

    if check_date(year, month, day):
        print(f'{year}-{month}-{day}')
        break
