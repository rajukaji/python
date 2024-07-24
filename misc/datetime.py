from datetime import datetime
#strftime() to format date into different forms
#strptime() to take the formatted dates and keep it into a date formate
def days_spent_together(date1, date2):
    print(datetime.now())
    d1 = datetime.strptime(date1, '%Y-%m-%d')#in the format== year-month-day
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    diff = d2 - d1
    return str(diff.days) + " days!"
print(days_spent_together(2024-2-30, 25-2-30))
