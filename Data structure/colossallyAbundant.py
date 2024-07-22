def is_colossally_abundant(n):
    num = [i for i in range(1, n) if n % i == 0]
    print(num)
    total = 1
    for i in num:
        total += i

    if total >= n:
        return True

    return False

print(is_colossally_abundant(6))