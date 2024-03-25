import pytest
from um import count

def test_count_single_um():
    assert count("hello, um, world") == 1

def test_count_multiple_um():
    assert count("um, um, um, hello") == 3

def test_count_um_case_insensitive():
    assert count("Um, um, uM, UM") == 4

def test_count_no_um():
    assert count("yummy") == 0

def test_count_um_within_word():
    assert count("rumbly") == 0

def test_count_um_with_punctuation():
    assert count("Hello! Um... um? World.") == 2

if __name__ == "__main__":
    pytest.main()
