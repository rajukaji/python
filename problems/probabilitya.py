def probability_of_a(s):
    return round(len([i for i in s.lower() if i == 'a'])/ len(s), 2)


print(probability_of_a('samsara'))