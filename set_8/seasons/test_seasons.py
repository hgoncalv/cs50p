import pytest
from datetime import date
from seasons import get_date_delta


def test_get_date_delta_valid_dates():
    valid_dates = [
        ("2000-01-01", "Twelve million, seven hundred eighty-seven thousand, two hundred minutes"),
        ("1995-12-15", "Fourteen million, nine hundred fifteen thousand, five hundred twenty minutes"),
    ]
    for input_date, expected_output in valid_dates:
        assert get_date_delta(input_date) == expected_output


def test_get_date_delta_invalid_dates():
    invalid_dates = ["1995-13-40", "2000-02-30", "2022/04/24", "not a date"]
    for invalid_date in invalid_dates:
        assert get_date_delta(invalid_date) is None

def test_get_date_delta_future_date():
    future_date = date.today().isoformat()
    assert get_date_delta(future_date) == "Zero minutes"

if __name__ == "__main__":
    pytest.main()
