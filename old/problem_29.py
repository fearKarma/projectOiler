# a^ b 
#a 2 <= 1000, b 2 <= 1000
# distinct numbers count

a = 100
b = 100

distinct = set()
temp = 0

for i in range(2,a + 1):
	for j in range(2,b + 1):
		distinct.add(i**j)

print(len(distinct))



