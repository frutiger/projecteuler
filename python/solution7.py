#!/usr/bin/env python3

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

from utils import *

def test():
    assert(prime(6)     == 13)
    assert(prime(10001) == 104743)

def result():
    return 104743

if __name__ == "__main__":
    print(result())

