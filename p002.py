#!/usr/local/bin/python

total = 0

f0, f1 = 0, 1

while f1 < 4000000:
    f0, f1 = f1, f0 + f1

    if f1 % 2 == 0:
        total += f1

print(total)
