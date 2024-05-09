### Find the sum of all the primes below two million. ###
### 142913828922 ###

import math

def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = [i for i in range(n+1) if sieve[i]]
    return primes

def sum_primes(n):
    primes = sieve_of_eratosthenes(n-1)i
    return sum(primes)

print(sum_primes(2000000))
    
