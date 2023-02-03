from um import count_ums


def test_1():
    assert count_ums('hello, um, world') == 1

def test_2():
    assert count_ums('yummy') == 0

def test_3():
    assert count_ums('um, um, um') == 3

def test_4():
    assert count_ums('um') == 1

def test_5():
    assert count_ums('um um') == 2

def test_6():
    assert count_ums('um um um') == 3

def test_7():
    assert count_ums('Um') == 1

def test_8():
    assert count_ums('uM') == 1

def test_9():
    assert count_ums('UM') == 1

