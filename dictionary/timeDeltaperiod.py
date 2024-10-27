from datetime import timedelta, datetime

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

print(timedelta(weeks=3))
# use keyword arguements
# use timedelta to calculate any time period
# to subract '-' any two times.

dt1 = datetime(2024, 2, 24)
weeks_4 = timedelta(weeks=4)
dt2 = dt1 + weeks_4
print(dt2)
print(type(dt2))