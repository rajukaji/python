#tuples in python
#constant
#ordered and unchangeable,
#related data

student = ("Bro", 21, "male")

print(student.count("Bro"))#how many times occurs
print(student.index("male"))#index of male

for x in student:
    print(x, end=" ")

if "Bro" in student:
    print("Bro is here!")

#other methods

tup = 1,
print(type(tup))

tup = 1, 2, 3, 4
print(type(tup))