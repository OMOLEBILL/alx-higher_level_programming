#!/usr/bin/python3
def system_arg(argv):
    n = len(argv)
    if n == 1:
        print("{:d} arguments.".format(n - 1))
        return
    else:
        if n == 2:
            print("{:d} argument:".format(n - 1))
            print("{:d}: {:s}".format((n - 1), argv[1]))
        else:
            print("{:d} arguments:".format(n - 1))
            for i in range(0, n):
                if i != 0:
                    print("{:d}: {:s}".format(i, argv[i]))
if __name__ == "__main__":
    import sys
    system_arg(sys.argv)
