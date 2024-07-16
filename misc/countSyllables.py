def count_syllables(word):
    new = word.split('-')
    return len(new)
        
    # write your code here

# take user input
word = input()

# call the function
print(count_syllables(word))