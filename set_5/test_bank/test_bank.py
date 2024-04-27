import bank

def test_value_hello():
    assert bank.value("Hello, world!") == 0

def test_value_hello_case_insensitive():
    assert bank.value("HELLO, world!") == 0

def test_value_h():
    assert bank.value("Hi there!") == 20

def test_value_h_case_insensitive():
    assert bank.value("hi there!") == 20

def test_value_other():
    assert bank.value("Goodbye!") == 100

def test_value_other_case_insensitive():
    assert bank.value("goodbye!") == 100
