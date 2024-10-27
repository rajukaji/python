# using strptime to parse strings as Dates
import datetime as dt
# https://strftime.org/
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# str p time, strptime, string parse time

date_string = '24/12/1994'
str_date_parse = dt.datetime.strptime(date_string, "%d/%m/%Y")
print(type(str_date_parse))
print(str_date_parse)

date_string_1 = '02-24-1990'
date_string_parse = dt.datetime.strptime(date_string_1, '%m-%d-%Y')
print(date_string_parse)


date_string_2 = '24/2/1995 10:24'
date_format = '%d/%m/%Y %H:%M'
date_string_2_parse = dt.datetime.strptime(date_string_2, date_format)
print(date_string_2)