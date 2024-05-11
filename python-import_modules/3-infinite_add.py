#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for idx in range(1, len(sys.argv)):
        total = total + int(sys.argv[idx])
    print("{}".format(total))
