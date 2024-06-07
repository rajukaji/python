fname= "rahu"
lname= "ketu"
fullName = fname + " " + lname
print(fullName)

#but this can be done with better approach with 

#formatting

full = f"{fname} {lname}"
#evaluated at run time
#f or F for formatting
#like %d in c
#we can put any valid expressions in between 
#curly braces {len(fname)}
#eg {2 + 2} etc,,, 
print(full)
