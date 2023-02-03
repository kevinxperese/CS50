from working import convert_time

def test_1():
    assert convert_time('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_2():
    assert convert_time('9 AM to 5 PM') == '09:00 to 17:00'

def test_3():
    assert convert_time('9 AM to 5PM') == ValueError
    assert convert_time('9AM to 5PM') == ValueError
    assert convert_time('9AMto 5PM') == ValueError
    assert convert_time('9 A to 5PM') == ValueError
    assert convert_time('9:78 AM to 5 PM') == ValueError
    assert convert_time('9 AM to 5:90 PM') == ValueError
    assert convert_time('13 AM to 5:90 PM') == ValueError
    assert convert_time('0 AM to 5:90 PM') == ValueError
