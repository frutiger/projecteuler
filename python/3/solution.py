#!/usr/bin/env python

import sys
sys.path.append("..")

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from utils import *

def largest_prime_factor(n):
  if n < 2:
    raise ValueError('less than 2: %d' % n)

  return prime_factors(n)[-1:][0]

print(largest_prime_factor(600851475143))
