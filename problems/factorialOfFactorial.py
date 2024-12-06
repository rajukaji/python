def factorial_of_factorials(n):

    fact_stack = 1  
    total_fact = 1

    for i in range(2, n+1):
        
        for j in range(2, i+1):
            fact_stack *= j

        total_fact *= fact_stack
        fact_stack = 1
    
    return total_fact


print(factorial_of_factorials(5))
# resulting 1! * 2! * 3! * 4! * 5!