def alternating_factorial(n):
    sum = 0

    for i in range(1, n+1):

        if i % 2 == 0:
            fact = 1
            for j in range(1, i + 1):
                fact *= j
            # print(fact)
            sum += fact
            continue

        if i % 2 != 0:
            fact1 = 1
            for j in range(1, i+1):
                fact1 *= j
            # print(fact1)
            sum -= fact1

    return sum


print(alternating_factorial(5))

#eg, 
# 4 should equal to - 1! + 2! - 3! + 4!
# add even number's factorial
# subract odd number's factorial
# problem from programiz