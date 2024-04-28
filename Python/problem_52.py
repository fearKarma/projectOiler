"""

	It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

	Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

def has_same_digits(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

def find_smallest_x():
    x = 1
    while True:
        if all(has_same_digits(x, i * x) for i in range(2, 7)):
            return x
        x += 1

result = find_smallest_x()
print("The smallest positive integer x is:", result)
