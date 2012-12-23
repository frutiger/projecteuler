#!/usr/bin/env python3

# Allows flexible starting directories
import os
import sys
sys.path.append(os.path.join(sys.path[0], ".."))

"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

from utils import *
import itertools

less_than_4_million = itertools.takewhile(lambda x: x < 4000000, fibonaccis())
evens = filter(lambda x: x%2==0, less_than_4_million)
print(sum(evens))

