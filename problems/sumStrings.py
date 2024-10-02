def sum_str(a, b):
    # happy coding !
    try:
        return str(int(a) + int(b))
    except:
        return a if a.isdigit() else b if b.isdigit() else '0'


print(sum_str('3', '4'))