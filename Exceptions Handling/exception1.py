#numbers = [1, 2]
#print(numbers[3])
#only 2 elements, but, trying to access the 3rd one, the
#list index out of range error

try:#if
    age = int(input("Age: "))
    xfactor = 10 / age #input 0 to get zerodivision error
    print("correct input!")
#except:
 #   print('The value entered is illegal') 
 # this is for all kinds of errors like undefined,,,, 
except ValueError: #else, 
    print("You didn't enter a valid age")
except ZeroDivisionError:
    print("Age cannot be zero!")
#we can also combine these 2 exceptions if the print are same. 
#except (ValueError, ZeroDivisionError):
else:
    print("No exceptions were thrown")
finally:
    print("this is always executed")#consider opening a file and closing a file, put the closing the file here
#handle value error exception
#its important to try to handle the exception errors to avoid program crashing

print("handled properly!")

#other error, IndexError