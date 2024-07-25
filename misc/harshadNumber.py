# Complete the code below

# define a function
#Harshad number is a number that is divisible by 
# the sum of its digits
# eg 18, 24
def is_harshad(number):
    #since the number is a string we have no problem in not converting it into string
    num = [int(i) for i in number]
    total = 0
    if int(number) % sum(num) == 0:
        return 'It is a Harshad Number' 
    else:
        return 'It is not a Harshad Number'


# call the function
number = input('Enter a number :: ')# takes string input only
result = is_harshad(number)
print(result)