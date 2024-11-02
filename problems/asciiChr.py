def digital_decipher(s, key):
    return ''.join(chr(ord(i) - key) for i in s)


# subract string s by key and return the new string

print(digital_decipher('Kathmandu', 1))