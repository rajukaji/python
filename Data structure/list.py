#lists
vowels = ['a', 'e', 'i', 'o', 'u']

matric = [[0, 1], [2, 3]]

#list of 100 zeros

zeros = [0] * 100

print(zeros)

combined = zeros + vowels

print(combined)

#list () and range() functions

print(list (range(20)))

print(list (range(1, 15)))

print(list("hello world"))#each characters is an item of the list now. 

print(len(list("Raju")))#list length

#list methods
listt = ['ram', 'shyam', 'hanuman']
listt.append("mangal")
print(listt)
list1 = ["man", "eve", "woman"]


listt.extend(list1)#extend the list add another list to a list
print(listt)

#copy method, doesn't take any arguements

list2 = list1.copy()#copy list1 to list2
print(list2)