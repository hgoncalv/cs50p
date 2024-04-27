import plates

def test_valid_plate():
    assert plates.is_valid("AB123") == True

def test_valid_plate_with_six_characters():
    assert plates.is_valid("ABC123") == True

def test_invalid_plate_too_short():
    assert plates.is_valid("A") == False

def test_invalid_plate_too_long():
    assert plates.is_valid("ABCDEFG") == False

def test_invalid_plate_contains_space():
    assert plates.is_valid("AB 123") == False

def test_invalid_plate_contains_period():
    assert plates.is_valid("AB.123") == False

def test_invalid_plate_contains_punctuation():
    assert plates.is_valid("AB!123") == False

def test_invalid_plate_contains_numeric_in_middle():
    assert plates.is_valid("AB1C23") == False

def test_invalid_plate_start_with_single_letter():
    assert plates.is_valid("A123") == False

def test_invalid_plate_start_with_number():
    assert plates.is_valid("1AB23") == False

def test_invalid_plate_start_with_zero():
    assert plates.is_valid("0AB123") == False
    assert plates.is_valid("A0B123") == False

def test_zero_placement():
    assert plates.is_valid("ABC012") == False
    # assert plates.is_valid("ABCD02") == True
    # assert plates.is_valid("ABCD20") == True
    # assert plates.is_valid("ABCD23") == True

def test_invalid_plate_contains_two_consecutive_numbers():
    assert plates.is_valid("AB12C3") == False

def test_invalid_plate_contains_three_consecutive_numbers():
    assert plates.is_valid("AB123C") == False
