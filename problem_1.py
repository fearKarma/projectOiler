# Problem 1
# find the sum of all the multiples of 3 or 5 below 1000
sq = []
for x in range(0,1000):
    if x % 3 == 0 or x % 5 ==0:
        sq.append(x)
print(sum(sq))
