#count()

str1 = 'aaaa bbbbbbbbb cccccccccccccc dddddddddddddddddd eeeeeeeeeeeeeeeeeeeee ffffffffffffff'

print(str1.count('a'))
print(str1.count('f'))



dic = {i: i.count(i[0]) for i in str1.split()}
#this is a master piece



print(dic)