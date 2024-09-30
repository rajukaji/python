def no_boring_zeros(n):
    # your code
    try:
        return int(str(n).rstrip('0'))
    except:
        return 0


print(no_boring_zeros(12340000000))