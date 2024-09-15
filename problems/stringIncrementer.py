def increment_string(strng):
    # st = ''
    # for i in range(len(strng) - 1, -1, -1):
    #     if strng[i].isdigit():
    #         st += strng[i]
        
    #     if strng[i].isalpha():
    #         break
    
    # st = st[::-1]
    # # print(st)
    
    # ls = strng.split(st)
    
    # st = int(st)
    # st += 1
    
    # return ls[0] + str(st)


    if strng == '':
        return '1'
    
    if strng.isalpha():
        return strng + '1'
      
    st = ''

    for i in range(len(strng) - 1, -1, -1):
        if strng[i].isdigit():
            st += strng[i]

        if strng[i].isalpha() or not strng[i].isdigit():
            break

    try:
        st = str(int(st[::-1]))
        ls = strng[:-len(st)]
        
        added = int(st) + 1
        if len(str(added)) > len(st) and ls[-1] == '0':
            return ls[:-1] + str(added)

        return ls + str(added)
    
    except:
        pass


#   codewars best solution
#  head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
    

print(increment_string('abc123'))

