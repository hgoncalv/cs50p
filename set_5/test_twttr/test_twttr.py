import twttr
import pytest

# USE pytest -s test_file to see prints

def test_shorten_empty_string():
    assert twttr.shorten("") == ""

def test_shorten_no_vowels():
    assert twttr.shorten("xyz") == "xyz"

def test_shorten_only_vowels():
    assert twttr.shorten("aeiou") == ""

def test_shorten_mixed_case():
    assert twttr.shorten("Hello World") == "Hll Wrld"

def test_shorten_with_vowels():
    assert twttr.shorten("Python is awesome!") == "Pythn s wsm!"

def test_shorten_with_repeated_vowels():
    assert twttr.shorten("aaeeii") == ""

def test_shorten_with_unicode_chars():
    assert twttr.shorten("éöüaäiï") == "éöüäï"

def test_shorten_without_capitalized_vowels():
    assert twttr.shorten("AEIOU") == ""

def test_shorten_does_not_modify_numbers():
    assert twttr.shorten("abc123def") == "bc123df"

def test_shorten_invalid_input():
    with pytest.raises(Exception) as exc_info:
        twttr.shorten(123)
    assert isinstance(exc_info.value, Exception)
    print("Exception type:", type(exc_info.value))
