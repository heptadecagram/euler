
def is_palindromic(num):
    myStr = str(num)
    revStr = myStr[::-1]
    return myStr == revStr

results = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if is_palindromic(i*j):
            results.append(i*j)

print(max(results))
