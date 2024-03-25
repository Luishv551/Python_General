from plates import is_valid

def test_isalnum():
    assert is_valid("CS5!") == False

def test_isalpha():
    assert is_valid("C550") == False
    assert is_valid("55") == False
    assert is_valid("50CS") == False

def test_size():
    assert is_valid("C55000") == False
    assert is_valid("H") == False
    assert is_valid("HH") == True

def test_letter():
    assert is_valid("C50A1") == False

def test_punctuation():
    assert is_valid("C5.91") == False
    assert is_valid("C5 91") == False

def test_just_letters():
    assert is_valid("OUTDATE") == False

def test_firstn_notzero():
    assert is_valid("CS05") == False
    assert is_valid("0S50") == False
    assert is_valid("00") == False
    assert is_valid("CS50") == True
    assert is_valid("CS505") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_justnumbers():
    assert is_valid("12345") == False
    assert is_valid("12") == False
