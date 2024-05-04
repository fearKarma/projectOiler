### Problem 6 ###
# sum of the first 10 squares 385
# the square of the sum of the first ten numers = 55^2 = 3025
# the difference between sum of squares and first ten numbers is 3025 - 385 = 2640
# find the difference between the sum of the squares of the first one hundred and the square of the sum

import math

def sumSquare():
    sq_sum = 0

    for x in range(1, 101):
            sq_sum += math.pow(x,2)

    return sq_sum

def sqSum():
    sq_sum_sq = 0

    for x in range(1,101):
        sq_sum_sq  += x

    return math.pow(sq_sum_sq, 2)

print(sqSum() - sumSquare())
