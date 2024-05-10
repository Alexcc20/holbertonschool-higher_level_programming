#!/usr/bin/python3
import sys

def add_arguments(*args):
    result = sum(int(arg) for arg in args)
    print(result)

if __name__ == "__main__":
    args = sys.argv[1:]
    add_arguments(*args)
