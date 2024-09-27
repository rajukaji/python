# # potential code before try catch

# try:
#      code to try to execute
# except ZeroDivisionError:
#      code to execute if there is a ZeroDivisionError
# except NameError:
#      code to execute if there is a NameError
# except:
#      code to execute if there is any exception
# else:
#      code to execute if there is no exception
# finally:
#      code to execute at the end of the try except no matter what
    
    
# # code that will execute if there is no exception or 
# # a one that we are handling

try:
    a = 1
    b = 0
    c = a // b
except ZeroDivisionError:
    # When zeroDivisionError occurs
    print('There was a zero division error!')


try:
    pass
except IndentationError:
    print('Your code is empty!')