#what is the 10 001st prime number

import math

def isPrime(x):
    if x <= 1:
        return False
    for w in range(2, int(math.sqrt(x)) + 1 ):
        if x % 2 == 0:
            return False
    return True

def ten_tho():
    n = 0
    p = 0
    while n <= 60:
        for g in range(0,50000000):
            if isPrime(g):
                n += 1
                print(g)
    return g

        


print(ten_tho())





