def odd(number):
    i = 0
    res = 0
    for _ in range(int(len(number) / 2)):
        res += 2 * number[i] * number[len(number) - i - 1]
        i += 1
    return res


def even(number):
    i = 0
    res = 0
    middle = int((len(number) + 1) / 2)
    for j in range(middle - 1):
        res += 2 * number[i] * number[len(number) - i - 1]
        i += 1
    res += number[middle - 1] ** 2
    return res


def catlina(number):
    res = []
    res.append(1)
    res.append(1)
    for i in range(2, number):
        if i % 2 == 0:
            res.append(odd(res))
        else:
            res.append(even(res))
    return res


print(catlina(10))
