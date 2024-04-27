# the Number, 197, is called a circular prime because all the rotation of the digits: 197 719 971, are themselves prime.
# 197 1972 19725 7197
# 719 2197 51972
# 971 7219 25197
#     9721 72519
#          97251
#          
#      
# there are 13 such primes below 100: 2,3,5,7,11,13,17,31,37,71,73,79 and 97

# how many circular primes are there below one million?

# make a is prime function
# make a function to rotate digits
# use prime function to check if number is still prime after rotations
# return that number if true

from math import sqrt

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def circulate(n):
    num_str = str(n)
    circular_shifts = [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))]
    return circular_shifts

def CheckCircPrime(n):
    circular_shifts = circulate(n)
    for shift in circular_shifts:
        if not isPrime(shift):
            return False
    return True

lsCirculars = [n for n in range(2,1000000) if CheckCircPrime(n)]

print(len(lsCirculars))
