
'''
os = laptops['os'].unique()
print(os)

mapping_dict = {'macOS': 'macOS', 'Mac OS' : 'macOS', 'No OS': 'No OS', 'Windows' : 'Windows', 'Linux' : 'Linux', 'Android': 'Android', 'Chrome OS': 'Chrome OS'}

laptops['os'] = laptops['os'].map(mapping_dict, na_action='ignore')
print(laptops['os'])

print(laptops['os'].value_counts())

'''