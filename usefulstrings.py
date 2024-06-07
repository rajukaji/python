text = " useful methods "
#use useful methods
print(text.upper())
print(text.lower())
print(text.title())#titile case
#first characters of every word shall be uppercase
print(text.strip())
#getting rid of white spaces at the beginning
#lstrip() or rstrip()
print(text.find("met"))#index position

print(text.replace("u", "P"))

print("use" in text)
#character in the text
print("help" not in text)