def BreakCamelCase(string_parameter):

    return ''.join(' ' + ch if ch.isupper() else ch for ch in string_parameter)


print(BreakCamelCase('helloCamelCase'))