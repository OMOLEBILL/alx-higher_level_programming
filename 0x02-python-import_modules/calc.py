
from calculator_1 import add, div, mul, sub
 
def calc(argv):
    n = len(argv) - 1
    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if c == "*" : 
        print("{:d} {:s} {:d} = {:d}".format(a, c, b, mul(a, b)))
    elif c == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, c, b, add(a, b)))
    elif c == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, c, b, sub(a, b)))
    elif c == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, c, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        
if __name__  == "__main__":
    import sys
    calc(sys.argv)
