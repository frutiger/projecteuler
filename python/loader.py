#!/usr/bin/env python3

import argparse
import importlib
import sys

NUM_PROBLEMS = 7

def test(problem):
    module = importlib.import_module("solution" + problem)
    module.test()

def result(problem):
    module = importlib.import_module("solution" + problem)
    print("Solution %s: %d" % (problem, module.result()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problems", metavar="n", type=int, nargs="*")
    parser.add_argument("--test", "-t", dest="action",
                        action="store_const", const=test, default=result)
    args = parser.parse_args()
    if len(args.problems) == 0:
        args.problems = range(1, NUM_PROBLEMS + 1)
    for i in args.problems:
        args.action(str(i))

