from working import convert

def test_1():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_2():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_3():
    assert convert('9 AM to 5PM') == ValueError
    assert convert('9AM to 5PM') == ValueError
    assert convert('9AMto 5PM') == ValueError
    assert convert('9 A to 5PM') == ValueError
    assert convert('9:78 AM to 5 PM') == ValueError
    assert convert('9 AM to 5:90 PM') == ValueError