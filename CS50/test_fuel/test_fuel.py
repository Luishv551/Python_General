import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50 and gauge(50) == '50%'
    assert convert("1/100") == 1 and gauge(1) == 'E'
    assert convert("99/100") == 99 and gauge(99) == 'F'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('3/2')
