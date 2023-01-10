from problemset5 import vanity_plates


def test_is_right_length():
    assert vanity_plates.is_right_length('a') == False
    assert vanity_plates.is_right_length('ab') == True
    assert vanity_plates.is_right_length('abc123') == True
    assert vanity_plates.is_right_length('abc1234') == False


def test_starts_with_two_letters():
    assert vanity_plates.starts_with_two_letters('abc') == True
    assert vanity_plates.starts_with_two_letters('ab3') == True
    assert vanity_plates.starts_with_two_letters('AbC') == True
    assert vanity_plates.starts_with_two_letters('a23') == False


def test_has_no_punctuation():
    assert vanity_plates.has_no_punctuation('abc123') == True
    assert vanity_plates.has_no_punctuation('abs!123') == False
    assert vanity_plates.has_no_punctuation('abs123.') == False
    assert vanity_plates.has_no_punctuation('?abs123') == False


def test_ends_with_numeric():
    assert vanity_plates.ends_with_numeric('foobar5') == True
    assert vanity_plates.ends_with_numeric('foobarS') == False  # This test found a bug in my original code!


def test_first_number_not_zero():
    assert vanity_plates.first_number_not_zero('abc') == True  # This test found a bug in my original code!
    assert vanity_plates.first_number_not_zero('0bc') == False
    assert vanity_plates.first_number_not_zero('abc123') == True
    assert vanity_plates.first_number_not_zero('abc012') == False

