from project import is_image_file, compare_hashes, check_path
import pytest
import os


# Test is_image_file function
def test_is_image_file_with_image_extensions():
    assert is_image_file("image.jpg") == True
    assert is_image_file("image.jpeg") == True
    assert is_image_file("image.png") == True
    assert is_image_file("image.bmp") == True
    assert is_image_file("image.gif") == True


def test_is_image_file_with_non_image_extensions():
    assert is_image_file("text.txt") == False
    assert is_image_file("document.docx") == False
    assert is_image_file("data.csv") == False


def test_is_image_file_with_wrong_type():
    assert is_image_file(123) == False
    assert is_image_file(["image.jpg"]) == False
    assert is_image_file({"file": "image.jpg"}) == False


def test_is_image_file_with_uppercase_extensions():
    assert is_image_file("image.JPG") == True
    assert is_image_file("image.PNG") == True


def test_is_image_file_with_mixed_case_extensions():
    assert is_image_file("image.JpEg") == True
    assert is_image_file("image.BmP") == True


# Test compare_hashes function
def test_compare_hashes_with_identical_hashes():
    assert compare_hashes("abcdef", "abcdef") == True
    assert compare_hashes("123456", "123456") == True


def test_compare_hashes_with_different_hashes():
    assert compare_hashes("abcdef", "abcde0") == False
    assert compare_hashes("123456", "123450") == False


def test_compare_hashes_with_wrong_type():
    assert compare_hashes(123, "abcdef") == False
    assert compare_hashes("abcdef", 123) == False


def test_compare_hashes_with_non_string_input():
    assert compare_hashes("abcdef", 123) == False
    assert compare_hashes(["abcdef"], "abcdef") == False
    assert compare_hashes({"hash": "abcdef"}, "abcdef") == False


# Test check_path function
def test_check_path_existing_file():
    assert check_path(__file__, is_folder=False) == True


def test_check_path_existing_folder():
    assert check_path(os.path.dirname(__file__), is_folder=True) == True


def test_check_path_non_existing_path():
    assert check_path("/non/existing/path") == False


def test_check_path_wrong_type():
    assert check_path(123, is_folder=False) == False


def test_check_path_invalid_folder():
    assert check_path(__file__, is_folder=True) == False


def test_check_path_invalid_file():
    assert check_path(os.path.dirname(__file__), is_folder=False) == False


def test_check_path_empty_string():
    assert check_path("", is_folder=False) == False
    assert check_path("", is_folder=True) == False


def test_check_path_none_input():
    assert check_path(None, is_folder=False) == False
    assert check_path(None, is_folder=True) == False
