#fibonacci
def fibo(nth):
    fib = [0, 1]
    while len(fib) <= nth:
        fib.append(fib[-2] + fib[-1]) #last term add 2nd last term

    return fib


print(fibo(10))
