
def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    else:
        return number
