def double_age(father_age, son_age):
    count = 0
    while True:
        if son_age*2 == father_age:
            return count
        count += 1
        son_age+=1
        father_age+=1

# father age is twice the son's age