def resto(n1):
    r1 = n1%3
    r2 = n1%5

    if r1 == 0 and r2 == 0:
        return 'FizzBuzz'
    elif r1 == 0:
        return 'Fizz'
    elif r2 == 0:
        return 'Buzz'
    else:
        return n1

exibe = resto(11)
print(exibe)