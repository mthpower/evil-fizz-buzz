from fizzbuzz.format_list_to_string import format_list_to_string_with_comma
from fizzbuzz.sequence_generator import sequence_generator
from fizzbuzz.fizzbuzz import fizzbuzz
import pytest

def test_generating_a_sequence():
    assert sequence_generator(1, 100) == range(1, 101)


@pytest.mark.parametrize('number', [1, 2, 4])
def test_numbers_are_not_replaced_otherwise(number):
    assert fizzbuzz(number) == number


@pytest.mark.parametrize('number', [3, 6, 9])
def test_multiples_of_three_produce_fizz(number):
    assert fizzbuzz(number) == 'fizz'


@pytest.mark.parametrize('number', [5, 10, 20])
def test_multiples_of_five_produce_buzz(number):
    assert fizzbuzz(number) == 'buzz'

@pytest.mark.parametrize('number', [15, 30, 45, 60])
def test_any_multiple_of_3_and_5_produce_fizzbuzz(number):
    assert fizzbuzz(number) == 'fizzbuzz'

def test_convert_array_to_comma_delimitted_string():
    assert format_list_to_string_with_comma([1,2,3,4,5]) == "1,2,3,4,5"
