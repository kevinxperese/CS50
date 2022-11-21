from home_federal_savings_bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello there!') == 0

def test_startswith_h():
    assert value('hippo') == 20
    assert value('howdy') == 20
    assert value('hell on earth') == 20

def test_not_hello_or_startswith_h():
    assert value('any thing else') == 100
    assert value(' hello') == 100
    assert value(' hell0') == 100
