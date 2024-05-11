#n = n / 2 if even
#n = 3n + 1 if odd
#number under 1 million that generates the largest chain


def collatz(n):
    x = []
    if n == 1:
        return n, len(x) 
    if n % 2 == 0
        x.append(n)
        collatz(n / 2) 
    collatz(3 * n + 1) 


