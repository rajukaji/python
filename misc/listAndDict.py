dic = {'c': 99, 'b': 98, 'a': 97}

print(dic)
sort = sorted(dic.items())
print(sort)
print(list(dic))
print(type(dic))
print(sort)
print(type(sort))
print(dict(sort))

dic = dict(sort)
print(type(dic))
value = []
key = []
for i in dic:
    value.append(i)
    key.append(dic[i])
    #print(dic[i])

print(value)
print(key)
print(list(value+ key))
listing = value + key
print(listing)
print([value, key])

word = 'bea-uti-ful'
print(word.split('-'))