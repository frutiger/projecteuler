#!/usr/bin/env python

import itertools

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

def fibonaccis():
  a, b = 0, 1
  while True:
    yield a
    b = a + b
    a = b - a

def fibonacci(x, y=None):
  if x < 1:
    raise ValueError('less than 1: %d' % x)

  if y is None:
    return list(itertools.islice(fibonaccis(), x - 1, x))[0]

  if y <= x:
    raise ValueError('not greater than %d: %d' % (x, y))

  return list(itertools.islice(fibonaccis(), x - 1, y - 1))

