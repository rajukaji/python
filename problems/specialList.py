def is_special(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            if lst[i] % 2 != 0:
                return False
        else:
            if lst[i] % 2 == 0:
                return False

    return True
    


# odd index has odd values
# even index has even values

print(is_special([1, 2, 3, 4, 5, 6]))

