def add_binary_strings(bin_str1, bin_str2):
    add = bin(int(bin_str1, 2) +int(bin_str2, 2) )
    return add[2:]


print(add_binary_strings("1010", '1100'))
