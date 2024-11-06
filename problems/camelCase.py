def to_camel_case(s):
    st = ''.join(i[0].upper() + i[1:] for i in s.split(' '))
    return st[0].lower() + st[1:]


print(to_camel_case('hello kathmandu nepal'))