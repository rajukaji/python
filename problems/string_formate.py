country = 'Nepal'

string = 'i am from ' + country + '!'
print(string)

# instead write, 

string = f"I am from {country}!"
# formatted string, or use a method
print(string)

string = 'I am from {}!'.format(country)
print(string)

_PI = 3.14156
print(f"{_PI:.2f}")
# decimal precision

nepal_total_area = 147181

print(f"{nepal_total_area:,}")
# use of thousand separator

# combining thousand separator and decimal precision

worth = 10000000000.0000111333
print(f"{worth:,.2f}")