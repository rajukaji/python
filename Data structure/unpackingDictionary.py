#unpacking with 2 **
dictionary = {"x": 1}
secondDictionary = {"x": 10, "y": 2}
#now combine both
combined = {**dictionary, **secondDictionary, "z": 1}#for the value of x last value, ie 10 is used
print(combined)

#note: cannot combine both list and dictionary though