#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 1:
    print("{:d} arguments.".format(0))
elif n > 1:
    print("{:d} arguments:".format(n-1))
    for i in range(0, n):
        if i != 0:
            print("{:d}: {:s}".format((i), sys.argv[i]))
