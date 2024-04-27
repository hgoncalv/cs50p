import pytest
from jar import Jar


def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom initialization
    jar = Jar(capacity=8)
    assert jar.capacity == 8
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(8)  # Attempt to deposit more than capacity
    assert jar.size == 5  # Size should remain unchanged


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    with pytest.raises(ValueError) as exc_info:
        jar.withdraw(8)  # Attempt to withdraw more than contents
    assert (
        str(exc_info.value) == "Not enough cookies in the jar"
    )  # Check if the correct exception message is raised
    assert jar.size == 5  # Size should remain unchanged

    with pytest.raises(ValueError) as exc_info:
        jar.withdraw(6)  # Attempt to withdraw more than contents
    assert (
        str(exc_info.value) == "Not enough cookies in the jar"
    )  # Check if the correct exception message is raised
    assert jar.size == 5  # Size should remain unchanged

    jar.withdraw(5)
    assert jar.size == 0  # Size should be 0 after withdrawing all cookies

    with pytest.raises(ValueError) as exc_info:
        jar.withdraw(1)  # Attempt to withdraw from an empty jar
    assert (
        str(exc_info.value) == "Not enough cookies in the jar"
    )  # Check if the correct exception message is raised
    assert jar.size == 0  # Size should remain unchanged

    with pytest.raises(ValueError) as exc_info:
        jar.withdraw(-1)  # Attempt to withdraw a negative amount
    assert (
        str(exc_info.value) == "Cannot withdraw a negative amount"
    )  # Check if the correct exception message is raised
    assert jar.size == 0  # Size should remain unchanged


def test_capacity():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.capacity = -1  # Attempt to set negative capacity

    with pytest.raises(ValueError):
        Jar(capacity=-1)  # Attempt to initialize with negative capacity

    jar = Jar()
    jar.capacity = 10
    assert jar.capacity == 10


def test_size():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.size = -1  # Attempt to set negative size

    jar = Jar()
    jar.size = 10
    assert jar.size == 10

    jar.size = 15
    assert jar.size == 12  # Size should be capped at capacity


if __name__ == "__main__":
    pytest.main()
