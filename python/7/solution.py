#!/usr/bin/env python3

# Allows flexible starting directories
import os
import sys
sys.path.append(os.path.join(sys.path[0], ".."))

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

from utils import *

if __name__ == "__main__":
    assert(prime(6)     == 13)
    assert(prime(10001) == 104743)
    print("Problem 7: 104743")

