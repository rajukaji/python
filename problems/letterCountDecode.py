def duplicate_encode(word):
    #your code here
    return ''.join(['(' if word.lower().count(i) == 1 else ')' for i in word.lower()])

print(duplicate_encode('kathmandu'))

#multiple letters count encode to ')'
#single letter count encode to '('