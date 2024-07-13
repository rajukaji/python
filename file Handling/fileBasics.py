#best to use try...finally
#or
#with...open...as

file = open('file.txt', 'r')
print(file.read())
file.close()

#we can do the same as 
try:
    file = open('file.txt')
    print(file.read())
finally:
    file.close()

#or we can try
with open('file.txt') as file:
#we need not close the file, its automatically closed here
    print(file.read(5))

# 'a' as append
# 'w' as write
