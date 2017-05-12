from fizzbuzz.format_list_to_string import format_list_to_string_with_comma
from fizzbuzz.sequence_generator import sequence_generator
from fizzbuzz.fizzbuzz import fizzbuzz


def test_generating_a_sequence():
    assert sequence_generator(1, 100) == range(1, 101)

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

def test_15_produce_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_30_produce_fizzbuzz():
    assert fizzbuzz(30) == 'fizzbuzz'

def test_any_multiple_of_3_and_5_produce_fizzbuzz():
    assert fizzbuzz(45) == 'fizzbuzz'
    assert fizzbuzz(60) == 'fizzbuzz'
    assert fizzbuzz(90) == 'fizzbuzz'

def test_convert_array_to_comma_delimitted_string():
    assert format_list_to_string_with_comma([1,2,3,4,5]) == "1,2,3,4,5"