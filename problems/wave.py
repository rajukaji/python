def wave(people):
    # Code here
    str = ''
    lst = []
    
    for i, k in enumerate(people):
#         count = 1
        
        if k == ' ':
            
            continue
            
        for j in range(len(people)):

            if j == i:
#                 if count == 1:
                str += people[j].upper()
#                 count += 1
                continue
            
#             if i == ' ':
#                 str += ' '
#                 continue
                
            str += people[j]
            
        lst.append(str)
        str = ''
    return lst
    #    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]



print(wave(['Kathmandu']))
