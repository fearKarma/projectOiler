#         rows
#  c       0  1  2  3  4
#  o   0  21  22 23 24 25
#  l   1  20  7  8  9  10
#  o   2  19  6  1  2  11
#  m   3  18  5  4  3  12
#  n   4  17  16 15 14 13

"""function solution(n) {
    n = (n - 1) / 2;
    return 2 * n * (8 * n * n + 15 * n + 13) / 3 + 1;
}
"""

def solution(n):
    n = (n - 1) / 2
    return 2 * n * (8 * n * n + 15 * n + 13) / 3 + 1

print(solution(1001))








