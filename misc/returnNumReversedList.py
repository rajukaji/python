def reverse_number_digits(num):
    reverseIt = [int(i) for i in str(num)]
    return reverseIt[::-1]
# take the user input
num = int(input('Enter a number :: '))

# call the function
print(reverse_number_digits(num))
