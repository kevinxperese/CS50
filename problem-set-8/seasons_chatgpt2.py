# Second try from ChatGPT

import sys
from datetime import datetime, timedelta


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)


def years_months_days_hours_minutes(td):
    years, days = divmod(td.days, 365)
    months = days // 30
    days = days % 30
    hours, remainder = divmod(td.seconds, 3600)
    minutes = (remainder + td.microseconds/1000000) // 60
    return years, months, days, hours, minutes


def to_words(years, months, days, hours, minutes):
    words = []
    if years:
        words.append(f"{years} {'year' if years == 1 else 'years'}")
    if months:
        words.append(f"{months} {'month' if months == 1 else 'months'}")
    if days:
        words.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours:
        words.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        words.append(f"{int(minutes)} {'minute' if minutes == 1 else 'minutes'}")
    return ' '.join(words)


def main():
    date_str = input("Please enter your date of birth (YYYY-MM-DD): ")
    birth_date = parse_date(date_str)
    today = datetime.today()
    age = today - birth_date
    if age.days < 0:
        print("You haven't been born yet!")
        sys.exit(1)
    age_in_minutes = round(age.total_seconds() / 60)
    words = to_words(*years_months_days_hours_minutes(age))
    print(f"You are {words} old, or approximately {age_in_minutes} minutes.")


if __name__ == "__main__":
    main()
