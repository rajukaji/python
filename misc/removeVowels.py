# replace ___ with your code

# define a function that removes vowels from passed string
def remove_vowels(string):

    # define a list of vowels to be removed
    vowels = 'aeiouAEIOU'

    # define blank new_string variable to hold new string without vowels
    new_string = ''

    # loop through each character in the string
    for char in string:

        # if the character is not in vowels, add it to the new_string
        if char not in vowels:
            new_string += char

    # print the new string
    return new_string


# define the string from which vowels are to be removed
string = 'A quick brown fox jumps over the lazy dog'

# call the function to remove vowels
print(remove_vowels(string))