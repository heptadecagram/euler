#!/usr/bin/python

from math import sqrt

ar = []
for i in range(2,int(sqrt(600851475143))):
    if  600851475143 % i == 0:
        for a in ar:
            if i % a == 0:
                break
        else:
            ar.append(i)

print(max(ar))
