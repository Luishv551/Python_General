import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 25:00 PM")

if __name__ == "__main__":
    pytest.main()
