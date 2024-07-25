# Complete the code below

# define a function
#the sum of the cube of the digits of the number is equal to the number
# eg, 370, 371
def is_armstrong(number):

    num = [int(i)**3 for i in number]
    if sum(num) == int(number):
        return 'It is an Armstrong Number'
    else:
        return "It is not an Armstrong Number"


# call the function
number = input('Enter a number :: ') #takes string input
result = is_armstrong(number)
print(result)