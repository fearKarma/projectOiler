# Problem 4.py
# find the largest palindrome made from the product(8) of two 3 digit numbers

def isDrome(x):
    y = str(x)
    y = y[::-1]

    if x == int(y):
        return True
    return False

seq = 0
for x in range(100, 999):
    for y in range(999, 100, -1):
        temp = x * y
        if isDrome(temp):
            if temp > seq:
                seq = temp
print(seq)











