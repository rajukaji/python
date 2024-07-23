def total_washing_time(times_per_day, months):
    t = times_per_day
    m = months

    total = (t * 21 * 30 * m) // 60
    sec = 0
    #if (t * 21 * 30 * m) % 60 != 0:
    sec = (t * 21 * 30 * m) % 60
    
    ret = str(total) + ' minutes and ' + str(sec) + ' seconds'
    # t times per day , for 30  * m months
    #21/60 minutes
    return ret
# 30 days in in a month 21 sec to wash one at a time 
print(total_washing_time(9, 7))

