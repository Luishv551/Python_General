from twttr import shorten

#Lower and Upper cases
def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'

#Punctuation
def test_punctuation():
    assert shorten('!?,.') == '!?,.'

#Numbers
def test_numbers():
    assert shorten('1234') == '1234'

def main():
    test_upper_lower_cases()
    test_punctuation()
    numbers()

if __name__ == "__main__":
    main()

