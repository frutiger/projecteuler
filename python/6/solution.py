#!/usr/bin/env python3

# Allows flexible starting directories
import os
import sys
sys.path.append(os.path.join(sys.path[0], ".."))

"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

from utils import *

def solve(n):
    total = sum(range(1, n + 1))
    return sum([i*(total - i) for i in range(1, n + 1)])

if __name__ == "__main__":
    assert(solve(10) == 2640)
    assert(solve(100) == 25164150)
    print("Problem 6: 25164150")

