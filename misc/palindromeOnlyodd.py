# Complete the code below

# define a function
def semi_reverse(string):
    line = ''
    splt = [i for i in string.split()]
    for i in splt:
        if len(i) % 2 != 0:
            line = line + i[::-1] + ' '
            continue
        line = line +i + ' ' 
    return line.rstrip()

# call the function
string = input('Enter a string :: ')
result = semi_reverse(string)
print(result)
#reverse only when the length of the split() of the line is odd