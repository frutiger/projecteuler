#!/usr/bin/env python

def prime_factors(n):
  if n < 2:
    raise ValueError('less than 2: %d' % n)

  candidate = 2
  factors = []
  while n != 1:
    if n % candidate == 0:
      n = n / candidate
      factors.append(candidate)
    else:
      candidate += 1
  return factors

def triangular_number(n):
  return int((n*n + n) / 2)
