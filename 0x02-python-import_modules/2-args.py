#!/usr/bin/python3
def print_arg(argv):
    n = len(argv)
    if n == 1:
        print("{:d} argument.".format(n))
    else:
        if n == 2:
            print("{:d} argument:".format(n))
        else:
            print("{:d} arguments:".format(n))
            for i in range(0, n):
                if i != 0:
                    print("{:d}: {:s}".format(i, argv[i]))
if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
