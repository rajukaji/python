# replace ___ with your code

# define a function to add 1 to the number
# represented by the digits list
def add_one(digits):
    string = ''.join(map(str, digits))
    num = list(str(int(string) + 1))
    num1 = [int(i) for i in num]
    return num1

digits = [8, 9, 9]
added_digits = add_one(digits)
print(added_digits)
