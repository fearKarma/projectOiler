""" 

	if p is the perimeter of a right angle triangle with integral length sides {a,b,c},
	there are exactly three solutions for p = 120
	{20,48,52}, {24,45,51}, {30,40,50}
	for which value of p <= 1000 is the number of solutions maximised?

	a^2 + b^2 = c^2
	p = a + b + c 

	120



"""
# Dictionary to store the count of solutions for each perimeter
import math

solutions_count = {}

# Iterate through all possible values of m and n
for m in range(2, 32):  # Upper limit for m derived from 1000 / (2 * sqrt(2))
    for n in range(1, m):  # Ensure m > n
        if (m - n) % 2 != 0 or math.gcd(m, n) != 1:
            continue  # Skip if m - n is odd or m and n are not coprime
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        perimeter = a + b + c
        while perimeter <= 1000:
            solutions_count[perimeter] = solutions_count.get(perimeter, 0) + 1
            a += m**2 - n**2
            b += 2 * m * n
            c += m**2 + n**2
            perimeter = a + b + c

# Find the perimeter with the maximum number of solutions
max_solutions_perimeter = max(solutions_count, key=solutions_count.get)

print("Perimeter with the maximum number of solutions:", max_solutions_perimeter)
print("Number of solutions:", solutions_count[max_solutions_perimeter])




