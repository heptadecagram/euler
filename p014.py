
cache=dict()

def collatz(n):
    count = 0
    num = n
    while n != 1:
        if n in cache:
            count += cache[n]
            break
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    cache[num] = count
    return count

largest = 0
largestKey = 1
for i in range(1,1000000):
    seqLen = collatz(i)
    if seqLen > largest:
        largest = seqLen
        largestKey = i
print(largestKey,largest)




