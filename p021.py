#!/usr/local/bin/python

from itertools import combinations
from prime import primes

def mult(col):
    prod = 1
    for f in col:
        prod *= f
    return prod

def prime_factors_of(n):
    for p in primes(n):
        (a, b) = divmod(n, p)
        while b == 0:
            yield p
            n = a
            (a, b) = divmod(n, p)
        if n == 1:
            break


def factors_of(n) :
    for i in range(1, n//2+1):
        if n % i == 0:
            yield i

def compositeFactors(primeFacList):
    print(primeFacList)
    for i in range(2,len(primeFacList)):
        print(i)
        sl = list(combinations(primeFacList,i))
        for k in sl:
            yield mult(k)
        print(sl)

for n in range(2, 20):
     compositeFactors(prime_factors_of(n))
#    print(list(prime_factors_of(n)))
