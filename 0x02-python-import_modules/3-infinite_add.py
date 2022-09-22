#!/usr/bin/python3
def add_sys(argv):
    n = len(argv)
    sum = 0
    for i in range(0, n):
        if i != 0:
            sum += int(argv[i])
    print("{:d}".format(sum))
if __name__ == "__main__":
   import sys
   add_sys(sys.argv)
