"""
	the first two consecutive numbers to have two dinstinct prime factors are:
		14 = 2 x 7
		15 = 3 x 5 

	the first three consecutive numbers to have three distinct prime factors are:

		644 = 2^2 x 7 x 23
		645 = 3 x 5 x 43
		646 = 2 x 17 x 19

	find the first four consecutive integers to have four distinct prime factors each. what is the first of these numbers

"""

def prime_factors_count(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)

def find_four_consecutive_integers():
    consecutive_count = 0
    n = 1

    while True:
        if (
            prime_factors_count(n) == 4 and
            prime_factors_count(n + 1) == 4 and
            prime_factors_count(n + 2) == 4 and
            prime_factors_count(n + 3) == 4
        ):
            return n

        n += 1

result = find_four_consecutive_integers()
print(result)
