def mubashir_cipher(text):   
    code = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n'}
    str = ''

    for i in text:
        for j, k in code.items():
            if i == j:
                str += k
            
            if i == k:
                str += j
        
        if i == ' ':
            str += ' '
    
    return str


print(mubashir_cipher('kathmandu'))