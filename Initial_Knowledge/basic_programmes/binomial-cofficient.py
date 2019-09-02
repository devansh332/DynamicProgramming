def bio(n, k):
    if k == 0 or k == n:
        return 1
    return bio(n - 1, k - 1) + bio(n - 1, k)


print(bio(5, 2))
