num = 123000123
#format this to have commas in the place of thousands
format = f"{num:,}"
print(format)

num = "{:,}".format(num)
print(num)