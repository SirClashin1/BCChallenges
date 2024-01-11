from __future__ import annotations
from beginnercodes.challenges import test
from sympy import factorint


def prime_factorization(number):
    ans = []

    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    while number > 1:
        for i in range(2, number+1):
            if number % i == 0 and isPrime(i):
                number //= i
                ans.append(i)
                break

    return ans


test(803, prime_factorization)
