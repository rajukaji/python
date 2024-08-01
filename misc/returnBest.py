def returnFunction(n):
    return n**2 if n > 0 else "Zero"

print(returnFunction(0))
print(returnFunction(5))

#return
#You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. If the word's length is even, 
# return the middle 2 characters.
def get_middle(s):
    n = len(s)
    return s[n//2] if n%2!=0 else s[n//2 -1]+s[n//2]

print(get_middle('kathmandu'))