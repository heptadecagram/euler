#!/usr/local/bin/python

from prime import primes

n = 0
for p in primes(1000000):
    n += 1
    if n > 10000:
        break

print(p)
