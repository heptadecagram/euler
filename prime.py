#!/usr/local/bin/python

def primes(limit=1000000):
    N = limit

    data = [True] * (N//2)
    yield 2

    for i,n in enumerate(data):
        if n:
            p = 2*i+3
            yield p
            for m in range(p+i, N//2, p):
                data[m] = False

