"""
The prime 41, can be written as the sum of six consecutive primes:
						
						2+3+5+7+11+13 = 41

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,  contains
21 terms, and is equal to 953

Which prime, below one-million, can be written as the sum of the most consecutive primes?

""" 


#step one. function to generate a list primes from one to limit (1000000)
def sleeve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for number in range(2, int(limit ** 0.5) + 1):
        if primes[number]:
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False
    return [index for index, isPrime in enumerate(primes) if isPrime]

def sumSumSum(primes, limit):
    max_count = 0
    max_prime = 0

    for i in range(len(primes)):
        count = 0
        prime_sum = 0
        j = i

        while j < len(primes) and prime_sum + primes[j] <= limit:
            prime_sum += primes[j]
            count += 1

            if count > max_count and prime_sum in primes:
                max_count = count
                max_prime = prime_sum

            j += 1

    return max_prime

# Example usage:
limit = 1000000  # Example limit for generating primes
primes = sleeve(limit)
result = sumSumSum(primes, limit)
print(f"The prime number with the most consecutive prime sums below {limit} is {result}.")






	
			




	



#step three
#step four