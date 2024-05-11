def get_triangle_number(n):
    return n * (n + 1) // 2

def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
    return count

def triangle_numbers_with_over_n_divisors(divisor_count):
    n = 1
    while True:
        triangle_num = get_triangle_number(n)
        if count_divisors(triangle_num) > divisor_count:
            yield triangle_num
        n += 1

x = triangle_numbers_with_over_n_divisors(500)
print(next(x))  # Get the first triangle number with over 500 divisors


