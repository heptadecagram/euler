def fact(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def NchooseM(n,k):
    return fact(n)//(fact(k)*fact(n-k))

print(NchooseM(40,20))
