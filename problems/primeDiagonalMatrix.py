def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

    
def is_prime_diagonal(matrix):
    prime = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                prime = isPrime(matrix[i][j])
    
    return 'Yes' if prime else 'No'


#from programiz challange
matrix = [[3, 0],
          [0, 2]]
print(is_prime_diagonal(matrix))