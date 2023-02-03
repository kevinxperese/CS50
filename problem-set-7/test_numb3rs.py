from numb3rs import validate_ip, validate_ip_no_re


def test_no_letters():
    assert validate_ip('a.b.c.d') == False
    assert validate_ip_no_re('a.b.c.d') == False

def test_correct_number_range():
    assert validate_ip('1.2.3.4') == True
    assert validate_ip('1.235.5.7') == True
    assert validate_ip('1.269.2.3') == False
    assert validate_ip('0.1.2.3') == True
    assert validate_ip('-1.-2.-3.-4') == False

    assert validate_ip_no_re('1.2.3.4') == True
    assert validate_ip_no_re('1.235.5.7') == True
    assert validate_ip_no_re('1.269.2.3') == False
    assert validate_ip_no_re('0.1.2.3') == True
    assert validate_ip_no_re('-1.-2.-3.-4') == False


def test_left_padding():
    assert validate_ip('001.000.2.003') == True
    assert validate_ip('01.00.2.03') == True

    assert validate_ip_no_re('001.000.2.003') == True
    assert validate_ip_no_re('01.00.2.03') == True