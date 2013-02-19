#!/usr/bin/env python3

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import itertools

from utils import *

def solve(num):
    return sum(itertools.takewhile(lambda x: x < num, primes()))

def test():
    assert(solve(2000000) == 142913828922)

def result():
    return 142913828922

if __name__ == "__main__":
    print(result())

