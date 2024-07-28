# Complete the code below

# define a function
def camel_to_snake_case(string):
    snake = ''
    for i in string:
        if i.isupper():
            snake = snake + '_' + i.lower()
            continue
        snake += i
    return snake


# call the function
string = input('Enter Camel Case :: ')# eg, johnLennon
result = camel_to_snake_case(string)# eg, john_lennon
print(result)