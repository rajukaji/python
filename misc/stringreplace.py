'''
Python String Replace
The str.replace() method in Python replaces a specified phrase with another specified phrase in a string. It is a built-in string method that returns a copy of the string where all occurrences of a substring are replaced with another substring.

Syntax: string.replace(old, new)

old: The substring to be replaced.
new: The replacement substring.
'''

string = 'hello'

replaced_string = string.replace('hello', 'buffalo')

print(string)
print(replaced_string)


print(string.replace('$', 'no_change'))
# no change

print(string.replace('h', 'b'))
# prints bello replacing 'h' with 'b'

print(string.replace('e', ' meow '))
# prints h meow llo

salary = '$1,000,000+'
print(salary.replace('$', ''))

salary = salary.replace('$', '')
salary = salary.replace(',', '')
salary = salary.replace('+', '')

print(salary)