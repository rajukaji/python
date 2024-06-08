#logical and or not

name = "ramuji"

#falsy values, 0 "" [] none, in python

if not name:
    print("Name is empty")
    
string = " "    #empty with space

if not string.strip():#strip to remove white spaces
    print("empty string")
    
age = 22
if age >= 19 and age < 65:
#can be written as 19 >= age < 65
    print("Eligible")
    
# like in math, 18 <= age < 65
#inequalities in math

age = 21

if 18 >= age <= 31:
    print("True")