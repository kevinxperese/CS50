from seasons import valid_date, calc_mins_since_bday, convert_num_to_text
import re
import pytest
from datetime import date


def test_valid_date():
    assert valid_date('2023-03-03') == True
    assert valid_date('March 3, 2023') == False

def test_mins_since_bday():
    today = date(2023, 3, 3)
    assert calc_mins_since_bday(today, '2023-03-03') == '0'
    assert calc_mins_since_bday(today, '2023-03-02') == '1440'

    with pytest.raises(ValueError):
        calc_mins_since_bday(today, '2023-13-01')

def test_convert_num_to_text():
    assert convert_num_to_text('8') == 'eight'
    assert convert_num_to_text('10') == 'ten'
    assert convert_num_to_text('12') == 'twelve'
    assert convert_num_to_text('34') == 'thirty-four'
    assert convert_num_to_text('40') == 'forty'
    assert convert_num_to_text('100') == 'one hundred'
    assert convert_num_to_text('102') == 'one hundred two'
    assert convert_num_to_text('111') == 'one hundred eleven'
    assert convert_num_to_text('123') == 'one hundred twenty-three'
    assert convert_num_to_text('1000') == 'one thousand'
    assert convert_num_to_text('1007') == 'one thousand, seven'
    assert convert_num_to_text('1010') == 'one thousand, ten'
    assert convert_num_to_text('5000') == 'five thousand'
    assert convert_num_to_text('5432') == 'five thousand, four hundred thirty-two'
    assert convert_num_to_text('10009') == 'ten thousand, nine'
    assert convert_num_to_text('10070') == 'ten thousand, seventy'
    assert convert_num_to_text('12345') == 'twelve thousand, three hundred forty-five'
    assert convert_num_to_text('123456') == 'one hundred twenty-three thousand, four hundred fifty-six'
    assert convert_num_to_text('1000000') == 'one million'
    assert convert_num_to_text('1000001') == 'one million, one'
    assert convert_num_to_text('1234567') == 'one million, two hundred thirty-four thousand, five hundred sixty-seven'
    assert convert_num_to_text('99999999') == 'ninety-nine million, nine hundred ninety-nine thousand, nine hundred ninety-nine'
    assert convert_num_to_text('999999999') == 'nine hundred ninety-nine million, nine hundred ninety-nine thousand, nine hundred ninety-nine'
