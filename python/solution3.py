#!/usr/bin/env python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from utils import *

def largest_prime_factor(n):
    if n < 2:
        raise ValueError("less than 2: %d" % n)

    return prime_factors(n)[-1:][0]

def test():
    assert(largest_prime_factor(13195)        == 29)
    assert(largest_prime_factor(600851475143) == 6857)

def result():
    return 6857

if __name__ == "__main__":
    print(result())

