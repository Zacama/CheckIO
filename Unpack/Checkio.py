def checkio(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)
