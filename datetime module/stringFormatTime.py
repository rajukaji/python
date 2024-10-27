from datetime import datetime

# strftime, str f time, string format time

dt_object = datetime(1984, 4, 22)
dt_string = dt_object.strftime('%m/%d/%Y')
print(dt_string)

dt_string = dt_object.strftime('%B %d, %Y')
print(dt_string)

dt_object_1 = '24/02/1998'
dt_object_1 = datetime.strptime(dt_object_1, '%d/%m/%Y')

dt_string_1 = dt_object_1.strftime('%B, %Y')
print(dt_string_1)