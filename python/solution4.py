#!/usr/bin/env python3

"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import *
import itertools

def unique_pairs(max):
    for a in range(max, 0, -1):
        for b in range(max, a - 1, -1):
            yield (a, b)

def solve(num_digits):
    largest_num = (10 ** num_digits) - 1
    return max(filter(is_palindrome, map(product,
                                         unique_pairs(largest_num))))

def test():
    assert(solve(2) == 9009)
    assert(solve(3) == 906609)

def result():
    return 906609

if __name__ == "__main__":
    print(result())

