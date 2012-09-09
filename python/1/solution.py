#!/usr/bin/env python

import sys
sys.path.append("..")

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from utils import *

def sum_of_multiples(max, divisor):
  return divisor * triangular_number(int((max - 1)/divisor))

print(sum_of_multiples(1000,  3) \
    + sum_of_multiples(1000,  5) \
    - sum_of_multiples(1000, 15)) # these would get double counted
