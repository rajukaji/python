def string_to_dict(s):
    #s = s.split(',')
    return dict(key_value_pair.strip().split(':') for key_value_pair in s.split(','))


new_dict = string_to_dict('fruit:apple, color:red, taste:sweet')
print(new_dict)