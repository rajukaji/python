def central_binomial_coefficient(n):
    def fact(num):
        if num == 1: 
            return 1
        return num * fact(num-1)
    
    return fact(2 * n) / (fact(n)**2)


    # (2n choose n )= (2n)! / ((n!)**2)


print(central_binomial_coefficient(5))