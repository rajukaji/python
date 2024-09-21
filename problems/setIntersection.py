def common_elements(set1, set2):
    set3 = []
    for i in set1:
        if i in set2:
            set3.append(i)
    return set(set3) if not len(set3) == 0 else None

print(common_elements({1, 2, 3, 4, 5}, {2, 3, 6, 9}))