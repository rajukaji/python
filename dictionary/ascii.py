def alphabet_position(text):        
    dic = {}
    asci = 97

    for i in range(1, 27):
        dic[chr(asci)] = i
        asci += 1
    text = 'aa bb cc dd ee'

    lst = [str(dic[i]) for i in text.replace(' ', '')]

    #print(lst)
    return print(' '.join(lst))

    # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()) is the same

# print(dic)

alphabet_position('The brown fox')
#alphabet_position()
        
# dic = {}
# asci = 97

# for i in range(1, 27):
#     dic[chr(asci)] = i
#     asci += 1
# text = 'aa bb cc dd ee'

# lst = [str(dic[i]) for i in text.replace(' ', '')]

# print(lst)
# print(' '.join(lst))