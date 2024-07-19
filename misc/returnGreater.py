def max_value(s):
    newlist = s.split()
    a = int(newlist[0])
    b = int(newlist[1])

    if (a * b) > (a + b):
        return a*b
    else:
        return a+b
    
str = '2 6'
print(max_value(str))
#if 2 * 6 is greater than 2 + 6? or false?
# 2 * 6 = 12
# 2 + 6 = 8
# 12 > 8, so 12 is returned
