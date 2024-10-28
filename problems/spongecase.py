def to_spongecase(text):

    string = ''.join(text.split(' '))
    lst_len = [len(i) for i in text.split(' ')]
    st=''

    count = 0
    ind = 0
    for i in range(len(string)):
        if count == lst_len[ind]:
            st+=' '
            count = 0
            ind += 1
        count += 1

        if i % 2 != 0:
            st += string[i].upper()

        else:
            st+= string[i].lower()
        
    
    return st


# space shouldn't matter
# alternative case
# aCaCaCaCaCa Ca CaA aC

print(to_spongecase('Kathmandu Valley Kantipuri Nagari'))
print(to_spongecase("learn to code"))