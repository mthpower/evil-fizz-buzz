from fizzbuzz.fizzbuzz import fizzbuzz


def test_an_empty_repo():
    assert True


def test_numbers_are_not_replaced_otherwise():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(4) == 4

def test_multiples_of_three_produce_fizz():
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(9) == 'fizz'
