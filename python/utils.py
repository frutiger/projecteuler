#!/usr/bin/env python3

import functools
import itertools
import math
import operator

def taker(generator):
    def take(x, y=None):
        if x < 1:
            raise ValueError("less than 1: {0}".format(x))

        if y is None:
            return list(itertools.islice(generator(), x - 1, x))[0]

        if y <= x:
            raise ValueError("not greater than {0}: {1}".format(x, y))

        return list(itertools.islice(generator(), x - 1, y - 1))
    return take

def primes():
    nums      = []
    candidate = 2

    while True:
        is_prime = True
        for num in nums:
            if candidate % num == 0:
                is_prime = False
                break
            if num > math.sqrt(candidate):
                break
        if is_prime:
            nums.append(candidate)
            yield candidate
        candidate += 1

prime = taker(primes)

def prime_factors(n):
    factors = []
    for prime in primes():
        if n == 1:
            break
        while n % prime == 0:
            n = n / prime
            factors.append(prime)
    return factors

def triangular_number(n):
    return int((n*n + n) / 2)

def fibonaccis():
    a, b = 0, 1
    while True:
        yield a
        b = a + b
        a = b - a

fibonacci = taker(fibonaccis)

def is_palindrome(n):
    chars = str(n)
    for i in range(int(len(chars)/2)):
        if chars[i] != chars[len(chars) - 1 - i]:
            return False
    return True

def product(sequence):
    return functools.reduce(operator.mul, sequence)

def collatz(n):
    if n <= 0:
        raise ValueError("less than 1: {0}".format(n))
    yield n
    while n is not 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        yield n

def gen_len(gen):
    return sum(1 for _ in gen)
