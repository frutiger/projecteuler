#!/usr/bin/env python3

# Allows flexible starting directories
import os
import sys
sys.path.append(os.path.join(sys.path[0], ".."))

"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import collections
import functools
import operator

from utils import *

def solve(n):
    if n < 1:
        raise ValueError('less than 1: %d' % n)

    if n == 1:
        return 1

    all_factors = collections.Counter()
    for number in range(2, n + 1)[::-1]:
        factors = collections.Counter(prime_factors(number))
        common_factors = all_factors & factors
        if common_factors != factors:
            all_factors = all_factors + factors - common_factors
    return functools.reduce(operator.mul, all_factors.elements())

if __name__ == "__main__":
    assert(solve(10) == 2520)
    assert(solve(20) == 232792560)
    print("Problem 5: 232792560")

