def is_string_identical(text_string):
    if len(set(text_string)) == 1:
        return True
    else:
        return False
    # write your code here

# take user input
text_string = input('Enter a word:: ')
# call the function
print(is_string_identical(text_string))