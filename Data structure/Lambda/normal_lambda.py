#lambda function
n = 10
print(lambda n: n*2)

doubleIt = lambda n: n*2

print(doubleIt(10))#pass the arguement cause its a function

#multiple args in a lambda

aPowerb = lambda a, b: a ** b
#note: the body of lambda can only have 1 expression, but, it can have as many as arguements it needs.

print(aPowerb(2, 3))
