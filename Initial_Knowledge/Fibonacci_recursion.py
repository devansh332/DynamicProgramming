"""
This Programme is capable of printing nth fibonacci Number
and i will be using **time** Module just to get real time idea how
much time will the recursion methos took to solve the problem


"""
from time import time

initial_time = time()


def fibonacci(number):
    if number < 1:
        return 1
    else:
        return number + fibonacci(number - 1)

print (f"997th fibonacci number is {fibonacci(997)} and it took {initial_time-time()}s")

"""
Some of the sample outputs are :
1.5th fibonacci number is 120 and it took 0.0s
2.50th fibonacci number is 30414093201713378043612608166064768844377641568960512000000000000 and it took 0.0s
3.700th fibonacci number is 245351 and it took -0.0009968280792236328s
4.997th fibonacci number is 497504 and it took 0.0s
Still Pretty Fast but it will reach maximum depth of recursion when we try to find Fibonacci number of 998
"""