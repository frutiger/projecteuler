#!/usr/bin/env python3

import argparse
import glob
import importlib
import sys

def num_problems():
    return len(glob.glob("solution*.py"))

def load(problem):
    try:
        module = importlib.import_module("solution" + problem)
        return module
    except:
        raise RuntimeError("Could not load problem {0}, check "
                           "'solution{0}.py' exists".format(problem))

def test(problem):
    load(problem).test()

def result(problem):
    print("Solution {0}: {1}".format(problem, load(problem).result()))

if __name__ == "__main__":
    problems = num_problems()
    parser = argparse.ArgumentParser(description="Load and execute solutions")
    parser.add_argument("problems", metavar="N", type=int, nargs="*",
                        help="One or more problems (there are {0}) - load all \
                              if none supplied".format(problems))
    parser.add_argument("-t", "--test", dest="action",
                        action="store_const", const=test, default=result,
                        help="Test solution instead of getting the result")
    args = parser.parse_args()
    if len(args.problems) == 0:
        args.problems = range(1, problems + 1)
    for i in args.problems:
        try:
            args.action(str(i))
        except RuntimeError as e:
            print(e)

