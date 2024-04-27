"""
The arithmetic sequence 1487,4817 ,8147  in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three
1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?


"""
from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_permutations():
    for num in range(1000, 10000):
        if is_prime(num):
            perms = set(permutations(str(num)))
            prime_perms = [int(''.join(p)) for p in perms if p[0] != '0' and is_prime(int(''.join(p)))]
            prime_perms.sort()
            for i in range(len(prime_perms) - 2):
                if prime_perms[i + 1] - prime_perms[i] == 3330 and prime_perms[i + 2] - prime_perms[i + 1] == 3330:
                    if not (prime_perms[i] == 1487 or prime_perms[i + 1] == 4817 or prime_perms[i + 2] == 8147):
                        return str(prime_perms[i]) + str(prime_perms[i + 1]) + str(prime_perms[i + 2])

result = find_prime_permutations()
print(result)






	

		

