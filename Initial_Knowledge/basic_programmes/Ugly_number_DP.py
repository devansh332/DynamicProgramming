def uglyNumber(n):
    result = [0] * n
    result[0] = 1
    i2, i3, i5 = [0, 0, 0]

    N2 = 2
    N3 = 3
    N4 = 5
    for l in range(1, n):
        result[l] = min(N2, N3, N4)
        if result[l] == N2:
            i2 += 1
            N2 = result[i2] * 2

        if result[l] == N3:
            i3 += 1
            N3 = result[i3] * 3

        if result[l] == N4:
            i5 += 1
            N4 = result[i5] * 5

    # return result[n] value
    return result[-1]


print(uglyNumber(150))
