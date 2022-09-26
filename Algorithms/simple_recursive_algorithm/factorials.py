# Factorials
"""
n! = (n-0) * (n-1) * (n-2) * (n-3) * (n-4)
120 = (5) * (4) * (3) * (2) * (1)
"""
import time


def fac0(n: int) -> int:
    ans = 1
    for i in range(n, 1, -1):
        ans *= i

    return ans


def iterative_factorial(n: int) -> int:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def recur_factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)
