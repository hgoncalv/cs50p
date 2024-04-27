from numb3rs import validate

def test_valid_ip():
    assert validate("192.168.1.1") == True

def test_invalid_ip():
    assert validate("256.0.0.1") == False

def test_invalid_format():
    assert validate("This is not an IP address: 192.168.1.1") == False

def test_invalid_octet():
    assert validate("192.168.1.300") == False

def test_max_octet():
    assert validate("255.255.255.255") == True

def test_shouldbetrue_octet():
    assert validate("140.247.235.144") == True

