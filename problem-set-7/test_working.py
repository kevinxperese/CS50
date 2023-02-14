from working import convert_time
import pytest


def test_works1():
    assert convert_time('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_works2():
    assert convert_time('9 AM to 5 PM') == '09:00 to 17:00'

def test_ValueErrors():
    # Each of these should throw a ValueError in convert_time()
    test_strings = [
        'foo',
        # '9 AM to 5 PM',    # This fails to raise an error, but pytest doesn't tell me which item in the list the test fails on...
        '900 AM to 500 PM',
        '9AM to 5PM',
        '9 AMto 5 PM',
        '9 A to 5PM',
        '9:78 AM to 5 PM',
        '9 AM to 5:90 PM',
        '13 AM to 5:90 PM',
        '0 AM to 5:90 PM',
    ]

    for test_string in test_strings:
        with pytest.raises(ValueError):
            convert_time(test_string)

def test_random_string():
    with pytest.raises(ValueError):
        convert_time('foo')

def test_missing_colons():
    with pytest.raises(ValueError):
        convert_time('900 AM to 500 PM')

def test_bad_spacing():
    with pytest.raises(ValueError):
        convert_time('9AM to 5PM')

def test_bad_spacing2():
    with pytest.raises(ValueError):
        convert_time('9 AMto 5 PM')

def test_bad_spacing3():
    with pytest.raises(ValueError):
        convert_time('9 AM to5 PM')

def test_bad_spacing4():
    with pytest.raises(ValueError):
        convert_time(' 9 AM to5 PM')

def test_bad_spacing5():
    with pytest.raises(ValueError):
        convert_time('9 AM to5 PM ')


def test_wrong_AM():
    with pytest.raises(ValueError):
        convert_time('9 A to 5PM')

def test_bad_minutes():
    with pytest.raises(ValueError):
        convert_time('9:78 AM to 5 PM')

def test_bad_minutes2():
    with pytest.raises(ValueError):
        convert_time('9 AM to 5:90 PM')

def test_bad_hours():
    with pytest.raises(ValueError):
        convert_time('13 AM to 5:00 PM')

def test_bad_hours2():
    with pytest.raises(ValueError):
        convert_time('0 AM to 5:00 PM')

