#test anagram
#eg , restful and fluster, are anagram as every letters are used by both, and the letters are only jumbled
#eg, silent, listen
#eg, astronomer, Moon starer

def are_anagrams(string1, string2):
    if set(string1.lower()) == set(string2.lower().replace(" ", "")):
        return True
    else:
        return False
    #lower() to lower all the letters
    #replace(" ", "") white space to remove white space

    # write your code here

# take the user input
string1 = input('Enter a word :: ')
string2 = input('Enter another word :: ')
# call the function
print(are_anagrams(string1, string2))