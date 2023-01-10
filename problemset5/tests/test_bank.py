from problemset5 import home_federal_savings_bank


def test_hello():
    assert home_federal_savings_bank.value('hello') == 0
    assert home_federal_savings_bank.value('hello there!') == 0


def test_startswith_h():
    assert home_federal_savings_bank.value('hippo') == 20
    assert home_federal_savings_bank.value('howdy') == 20
    assert home_federal_savings_bank.value('hell on earth') == 20


def test_not_hello_or_startswith_h():
    assert home_federal_savings_bank.value('any thing else') == 100
    assert home_federal_savings_bank.value(' hello') == 100
    assert home_federal_savings_bank.value(' hell0') == 100
