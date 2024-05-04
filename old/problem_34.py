# 145 is a curious number, as 1! + 4! + 5 = 1 + 24 + 120 = 145!

# .

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 and are not sums they are not included.

# loop through numbers 
# split numbers into there individual digits
# add up the factorial of each digit and see if it adds up to the original number
#if they do add the number to a variable to sum all the numbers whos factorials add up to the original number
#

# factorial is start at number then add all numbers descending untl 1
def MakeFactorial(n):
    fact = 1
    for i in range (n,1,-1):
        fact *= i
    return fact

def SplitNumber(n):
   lnum = [int(d) for d in str(n)]

   return lnum

def checkFactorial(n):
    tr = 0
    fat = SplitNumber(n)
    for i in fat:
        tr += MakeFactorial(i)
    if n == tr:
        return True
    else:
        return False
test = 0
test2 = 0

for i in range(3,100000000000000):
    test = checkFactorial(i)
    if test == True:
        test2 += i
        print(str(i) + " is the sum of its digits sum factorial")
        print(test2)

