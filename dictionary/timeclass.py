# datetime.time(hour=0, minute=0, second=0, microsecond=0)

import datetime as dt

time_string = '8:00'
time_dt = dt.datetime.strptime(time_string, '%H:%M')
print(time_dt)

time_t = time_dt.time()
print(time_t)