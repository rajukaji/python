def rot13(message):
    
    st = ''
    
    for i in message:
        if i.isalpha():
            if ord(i) > 77 and ord(i) < 91:
                st += chr(ord(i) - 13)
                continue
                
            if ord(i) > 109 and ord(i) < 123:
                st += chr(ord(i) - 13)
                continue
            
            st += chr(ord(i) + 13)
        
        if not i.isalpha():
            st += i
        
    return st

#from codewars
#rotate 13 encoding,

print(rot13('hello world'))