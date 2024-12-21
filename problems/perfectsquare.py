import math
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
    

print(is_perfect_square(44))