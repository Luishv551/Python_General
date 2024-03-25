from bank import value

def test_return_0():
    assert value("hello bob") == 0
    assert value("Hello") == 0
    assert value("HeLLo BoB") == 0

def test_return_20():
    assert value("Hi") == 20
    assert value("hey") == 20

def test_return_100():
    assert value("What's up?") == 100
    assert value("good morning") == 100
