#lets define a function
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age

#calculate_xfactor(-1)#programme crashes 

#lets use try block

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

#all this is to avoid the crashing of the program