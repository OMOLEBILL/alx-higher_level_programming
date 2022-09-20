#!/usr/bin/python3
i = 122
while i >= 97:
    n = 0
    if i % 2 != 0:
        i -= 32
        n = 1
    print("{:s}".format(chr(i)), end="")
    if n == 1:
        i += 32
    i -= 1
