#!/usr/bin/python3
def argx_print(argv):
    n = len(sys.argv)
    if n == 1:
        print("{:d} arguments.".format(n - 1))
    elif n > 1:
        print("{:d} arguments:".format(n - 1))
        for i in range(0, n):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
if __name__ == "__main__":
    import sys
    argx_print(sys.argv)

