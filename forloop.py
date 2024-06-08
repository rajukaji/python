#we only have for loops and while loops in python

for x in "Python":#string iteration
    print(x)
    
    
for x in ['a', 'e', 'i', '0', 'u']:#loop list
    print(x)
    
#loop over sequence of numbers
#use built in range function
for x in range(5):
    print(x)
    
    
for x in range(3, 5):#from 3 to 4
    print(x)
    
for i in range(0, 10, 2):#step methon
    print(i)
    
#ctrl + / to comment 

print(range(5))
print(type(range(5)))#range object are iterable like strings and lists

print([1, 2, 3, 4, 5])

#range objects takes very small amout of memory