#!/usr/bin/env python3

import argparse
import glob
import importlib
import sys

def num_problems():
    return len(glob.glob("solution*.py"))

def test(problem):
    module = importlib.import_module("solution" + problem)
    module.test()

def result(problem):
    module = importlib.import_module("solution" + problem)
    print("Solution %s: %d" % (problem, module.result()))

if __name__ == "__main__":
    problems = num_problems()
    parser = argparse.ArgumentParser(description="Load and execute solutions")
    parser.add_argument("problems", metavar="N", type=int, nargs="*",
                        help="One or more problems (there are %d) - load all \
                              if none supplied" % problems)
    parser.add_argument("-t", "--test", dest="action",
                        action="store_const", const=test, default=result,
                        help="Test solution instead of getting the result")
    args = parser.parse_args()
    if len(args.problems) == 0:
        args.problems = range(1, problems + 1)
    for i in args.problems:
        args.action(str(i))

