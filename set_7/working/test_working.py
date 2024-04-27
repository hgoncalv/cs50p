import pytest
from working import convert

def test_convert_valid_input():
    assert convert("12:30 PM to 3:45 PM") == "12:30 to 15:45"
    assert convert("8:15 AM to 11:00 AM") == "08:15 to 11:00"
    assert convert("9:00 PM to 2:30 AM") == "21:00 to 02:30"

def test_convert_missing_minutes():
    assert convert("12 PM to 3 PM") == "12:00 to 15:00"
    assert convert("8 AM to 11 AM") == "08:00 to 11:00"
    assert convert("9 PM to 2 AM") == "21:00 to 02:00"

def test_convert_single_digit_hours():
    assert convert("7 AM to 9 PM") == "07:00 to 21:00"
    assert convert("11 AM to 1 PM") == "11:00 to 13:00"
    assert convert("6 PM to 8 AM") == "18:00 to 08:00"

def test_convert_invalid_input_no_to():
    with pytest.raises(ValueError):
        convert("12:30 PM 3:45 PM")  # Missing " to "

def test_convert_invalid_input_out_of_range():
    with pytest.raises(ValueError):
        convert("13:30 PM to 3:45 PM")  # Hour out of range
    with pytest.raises(ValueError):
        convert("12:30 PM to 13:45 PM")  # Hour out of range

