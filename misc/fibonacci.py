#fibonacci
def fibo(nth):
    fib = [0, 1]
    while len(fib) <= nth:
        fib.append(fib[-2] + fib[-1]) #last term add 2nd last term

    return fib


print(fibo(10))

def fibonacci(n):
    fib = [0, 1]
    if n == 1:
        return [fib[0]]

    for i in range(n-2):
        fib.append(fib[-1] + fib[-2])
    
        
    return fib

print(fibo(10))
