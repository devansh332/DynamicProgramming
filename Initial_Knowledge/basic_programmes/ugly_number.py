def is_divisible(number, divisor):
    return True if number % divisor == 0 else False


def ugly_number(number):
    prime_number = [2, 3, 5]
    for i in prime_number:
        while is_divisible(number, i):
            number = number // i
    if number == 1:
        return True
    else:
        return False


value = 0
i = 1
while (value != 150):
    if ugly_number(i):
        value += 1
    i += 1

print(i - 1)
