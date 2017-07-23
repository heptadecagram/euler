#!/usr/local/bin/python

for a in range(1, 500):
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c <= b:
            break

        if a**2 + b**2 == c**2:
            print(a*b*c)
