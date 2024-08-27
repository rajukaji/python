def high(x):
    # Code here
    greatest = 0
    sum = 0
    index = 0
    
    for ind, value in enumerate(x.split()):
        #enumerate as we want index as well as value, we split the sentence
        for j in value:
            sum = sum + ord(j) - 96
            #to calculate the sum of all the letters of the word
        
        if greatest < sum:
            greatest = sum
            index = ind
        #if greatest is less then the sum of a value
        #we need index for that greatest sum word, that should be used to return 
        
        sum = 0

    return x.split()[index]

    #return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k)) 
    #single line best solution in codewars


print(high('hello this is a taxi stand'))