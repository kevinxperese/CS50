import pytest
from datetime import date
from seasons_chatgpt4 import calculate_age_in_minutes, spell_out_minutes


def test_calculate_age_in_minutes():
    # Test case where the birthdate is today
    assert calculate_age_in_minutes(date.today()) == 0

    # Test case where the birthdate is one year ago
    assert calculate_age_in_minutes(date.today().replace(year=date.today().year - 1)) == 525600

    # Test case where the birthdate is 18 years ago
    assert calculate_age_in_minutes(date.today().replace(year=date.today().year - 18)) == 9460800


def test_spell_out_minutes():
    # Test case where the age is exactly zero minutes
    assert spell_out_minutes(0) == "zero minutes"

    # Test case where the age is less than zero (i.e., not born yet)
    assert spell_out_minutes(-1) == "not born yet"

    # Test case where the age is one minute
    assert spell_out_minutes(1) == "one minute"

    # Test case where the age is 59 minutes
    assert spell_out_minutes(59) == "fifty-nine minutes"

    # Test case where the age is one hour
    assert spell_out_minutes(60) == "one hour"

    # Test case where the age is 23 hours and 59 minutes
    assert spell_out_minutes(23 * 60 + 59) == "twenty-three hours fifty-nine minutes"

    # Test case where the age is one day
    assert spell_out_minutes(24 * 60) == "one day"

    # Test case where the age is 364 days
    assert spell_out_minutes(364 * 24 * 60) == "three hundred sixty-four days"

    # Test case where the age is one year
    assert spell_out_minutes(365 * 24 * 60) == "one year"

    # Test case where the age is 2 years, 30 days, 12 hours, and 15 minutes
    assert spell_out_minutes(2 * 365 * 24 * 60 + 30 * 24 * 60 + 12 * 60 + 15) == "two years thirty days twelve hours fifteen minutes"

    # Test case where the age is 99 years, 364 days, 23 hours, and 59 minutes
    assert spell_out_minutes(99 * 365 * 24 * 60 + 364 * 24 * 60 + 23 * 60 + 59) == "ninety-nine years three hundred sixty-four days twenty-three hours fifty-nine minutes"

    # Test case where the age is greater than 100 years
    assert spell_out_minutes(101 * 365 * 24 * 60 + 5 * 24 * 60 + 6 * 60 + 7) == "one hundred one years five days six hours seven minutes"
