def print_last_digit(number):
    srtnum = str(number)
    last = srtnum[-1]
    print("{:d}".format(int(last)), end="")
    return(int(last))
