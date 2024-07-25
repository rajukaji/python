# Complete the function below

# define a function
def is_palindrome(string):
    
    st = [i.lower() for i in string if (i.isalpha() or i.isdigit() )]

    if st == st[::-1]:
        return 'String is Palindrome'
    else:
        return "String is not Palindrome"


# call the function
string = input('Enter any string :: ')
result = is_palindrome(string)
print(result)