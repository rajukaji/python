#numbers = [1, 2]
#print(numbers[3])
#only 2 elements, but, trying to access the 3rd one, the
#list index out of range error

try:#if
    age = int(input("Age: "))
    print("correct input!")
except ValueError: #else, 
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
#handle value error exception
#its important to try to handle the exception errors to avoid program crashing

print("handled properly!")