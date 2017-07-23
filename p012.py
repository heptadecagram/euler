from prime import primes
from euler import fact

PRIMES = list(primes())

def pfac(num):
    p = 1
    nf = []
    #for i in range(1 + int(num**0.5)):
    for p in PRIMES:
        while num % p == 0:
            nf.append(p)
            num //= p
        if num == 1:
            break
    return nf

def NchooseM(n,k):
    return fact(n)//(fact(k)*fact(n-k))

def sumChoices(n):
    sum = 0
    for i in range(n+1):
        sum += NchooseM(n,i)
    return sum

# triangle #, factors
found = False
ind = 2
while not found:
    tri = sum(range(ind))
    pfactors = pfac(tri)
    t = sumChoices(len(pfactors))
    print(tri, pfactors, t)
    if t >= 500:
        found = True
        print("****")
        print(tri)
    ind += 1
