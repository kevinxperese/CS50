from jar import Jar
import pytest

def test_valueerror():
    with pytest.raises(ValueError):
        Jar(capacity=-4)

def test_valueerror2():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(13)

def test_valueerror3():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12

def test_size():
    jar = Jar()
    assert jar.size == 0

def test_deposit():
    jar = Jar()
    jar.deposit(1)

    assert jar.size == 1

def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    jar.withdraw(1)

    assert jar.size == 0

def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
