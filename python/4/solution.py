#!/usr/bin/env python

import sys
sys.path.append("..")

"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import *
import itertools

def unique_pairs(max):
  for a in range(max, 0, -1):
    for b in range(max, a - 1, -1):
      yield (a, b)

print(max(filter(is_palindrome, map(product, unique_pairs(999)))))

