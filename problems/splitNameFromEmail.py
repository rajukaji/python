def get_name_from_email(email):
    return ' '.join(email.split('@')[0].split('.'))

print(get_name_from_email('kathmandu.Nepal@social.com'))