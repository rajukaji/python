def count_letters(word):
    count = {}
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print(count_letters('gorupentumottugobarubunguru'))
