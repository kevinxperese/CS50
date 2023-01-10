from problemset5 import twttr


def test_shorten():
    assert twttr.shorten('kevin') == 'kvn'


def test_capitalization():
    assert twttr.shorten('Kurt') == 'Krt'


def test_sentence():
    assert twttr.shorten('I Love testing in Python!') == ' Lv tstng n Pythn!'