str = 'I love python programming'
print(str.split())#important concept
print(str.split()[::-1])

print(type(str))#string type
print(type(str.split()))#list type

str1 = ""
for i in str.split()[::-1]:
    #print(str1)
    str1 = str1 + i + ' '

print(str1)

print(str)
str = 'python'
print(str.split())
#split take default separator, sep = ' '   , ie space
print(str.split(':'))


