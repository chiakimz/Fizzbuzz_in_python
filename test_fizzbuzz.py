import fizzbuzz

def test_returns_fizz_with_3():
    assert fizzbuzz.Fizzbuzz(3) == 'fizz'

def test_returns_fizz_with_6():
    assert fizzbuzz.Fizzbuzz(6) == 'fizz'

def test_returns_buzz_with_5():
    assert fizzbuzz.Fizzbuzz(5) == 'buzz'

def test_returns_buzz_with_10():
    assert fizzbuzz.Fizzbuzz(10) == 'buzz'


def test_returns_fizzbuzz_with_15():
    assert fizzbuzz.Fizzbuzz(15) == 'fizzbuzz'

def test_returns_fizz_with_30():
    assert fizzbuzz.Fizzbuzz(30) == 'fizzbuzz'
