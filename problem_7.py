### What is the 10,001st prime number ###

import math

def isPrime(x):
    if x <= 1:
        return False
    for w in range(2, int(math.sqrt(x)) + 1 ):
        if x % w == 0:
            return False
    return True

def ten_tho():
    n = []
    g = 0
    while len(n) < 10001:
        if isPrime(g):
            n.append(g)
        g+=1
    return n

for x in ten_tho():
    print(x)





