#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

import math

def isPrime(x):
    if x <= 1:
        return False 
    for w in range(2, int(math.sqrt(x)) + 1):
        if x % w == 0:
            return False
    return True        

def factors(n):
    se = 0
    for x in range (1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            if isPrime(x):
                if se < x:
                    se = x
    return se

print(factors(600851475143))
