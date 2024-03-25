import pytest
from numb3rs import validate

def test_valid_ipv4():
    # Test a valid IPv4 address
    assert validate("255.255.255.255") == True

    # Test if only the first byte is checked
    assert validate("255.512.512.512") == False
    assert validate("512.255.255.255") == False
    assert validate("512.512.255.255") == False
    assert validate("512.512.512.255") == False
