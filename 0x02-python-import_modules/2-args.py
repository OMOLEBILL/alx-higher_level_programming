#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print("{:d} arguments.".format(n - 1))
    else:
        if n == 2:
            print("{:d} argument.".format(n - 1))
        else:
            print("{:d} arguments:".format(n - 1))
            for i in range(0, n):
                if i != 0:
                    print("{:d}: {:s}".format(i, sys.argv[i]))
