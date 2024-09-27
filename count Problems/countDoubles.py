def duplicate_count(text):

    count = 0
    text = text.lower()

    try:
        lst = {i: text.count(i) for i in text}

        value = lst.values()
        
        for i in value:
            if i > 1:
                count += 1

    except:
        pass
    
    return count

    # one line code from codewars
    # return len([c for c in set(s.lower()) if s.lower().count(c)>1])


print(duplicate_count('aabbbcdeeefffg11144433456'))


# count doubles
# aa = 2
# aa, bbb, eee, fff -> 4 that are more than 1
# hence, should return 4 counts for doubles that are seen in teh string

# text = 'aabbbcdeeefffg'
# lst = {i: text.count(i) for i in text}
# print(lst)