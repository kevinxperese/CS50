from um import count


def test_1():
    assert count('hello, um, world') == 1

def test_2():
    assert count('yummy') == 0

def test_3():
    assert count('um, um, um') == 3

def test_4():
    assert count('um') == 1

def test_5():
    assert count('um um') == 2

def test_6():
    assert count('um um um') == 3

def test_7():
    assert count('Um') == 1

def test_8():
    assert count('uM') == 1

def test_9():
    assert count('UM') == 1

