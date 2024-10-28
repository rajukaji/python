def capital_split(s):
    st = ''
    flag = 0

    for i in s:
        if i == ' ':
            flag = 0
        flag += 1

        if i.isupper():
            if flag == 1:
                st += i
                flag = 0
            else:
                st = st + '-' + i
            continue
        st += i
    return st.strip().split('-') if not st.islower() else []

# split a string at capital letter

print(capital_split('HelloKathmanduHelloHello'))