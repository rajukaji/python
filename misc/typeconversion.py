x = input("x :: ")#Its a string input
#typeerror
#y = x + 1
#entering an int will generate an error
#it doesn't do implicit type conversion
#so python is a strongly typed language

print(int(x))#type conversion
print(float(x))
print(bool(x))

#falsy values
#"" empty
#0 null value
#[]
#None (null) 
#boolean gives false
print(bool(0))#gives false
print(bool(1))
print(bool(-1))#is true
print(bool("string"))#this is true as well, non empty