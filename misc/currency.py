# define the function
def add_commas(number):
    # write your code here
    return "{:,}".format(number)
# take user input
number = int(input('Enter a number:: '))
# call the function
print(add_commas(number))