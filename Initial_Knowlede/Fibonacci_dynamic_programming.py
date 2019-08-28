"""
This Program is capable of printing nth fibonacci Number
and i will be using **time** Module just to get real time idea how
much time will the DP method took to solve the problem


"""
from time import time

initial_time = time()


def fibonacci(number):
    result = [0] * (number + 1)
    result[0], result[1] = 1, 1
    for i in range(2, number + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[number]


print(f"99th fibonacci number is {fibonacci(9999)} and it took {initial_time - time()}s")

"""
Some of the sample outputs are :
1.99th fibonacci number is 354224848179261915075 and it took 0.0s
2.999th fibonacci number is  and it took 0.0s
3.9999th fibonacci number is  and it took -0.005982875823974609s

By Trading some space we can get out of the limitation of maximum recursion dept and its faster then compared to recursion method as 

Recursion : O(e^n)
DP : O(N)

"""