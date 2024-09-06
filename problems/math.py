def id(a): return a

def zero(f=id): return f(0) #your code here
def one(f=id): return f(1)#your code here
def two(f=id): return f(2) #your code here
def three(f=id): return f(3) #your code here
def four(f=id): return f(4) #your code here
def five(f=id): return f(5) #your code here
def six(f=id): return f(6) #your code here
def seven(f=id): return f(7) #your code here
def eight(f=id): return f(8) #your code here
def nine(f=id): return f(9) #your code here

def plus(b): return lambda a: a + b #your code here
def minus(b): return lambda a: a - b #your code here
def times(b): return lambda a: a * b #your code here
def divided_by(b): return lambda a: a // b #your code here

print(nine(plus(nine())))
print(two(minus(four())))
print(three(times(five())))
print(eight(divided_by(four())))

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3