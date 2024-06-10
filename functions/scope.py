#local and global
#we dont  have block level scope in python
glob = "b" #global variable
#avoid using global variable
#even if you are using, avoid modifying it in a function
message = "a"


def greet():
    if True:
        #global message , we can do this to make it global, but, bad practice
        message = "b"#local variable
    print(message)#is accessible
    
    
print(message)