p = 29
g = 5 
b = 17
a = 12

B = g**b % p
print(B)

A = g**a % p
print(A)

calc = B**a % p
print(calc)

calc1 = A**b % p
print(calc1)
# calculating cryptography Diffie-Hellman key exchange,
# in the form of    B = g**b % p
# where g is the generator, b is the private key, p is the prime number
# B is the public key   B = g**b % p
# A is the public key of the other party, A = g**a % p
# the shared secret key
# K = A**b % p = B**a % p
# K = g**(ab) % p


'''
Alice and Bob agree on the public variables: a large prime number p and a generator g, where 0 < g < p. These values will be disclosed publicly over the communication channel. Although insecurely small, we will choose p = 29 and g = 3 to simplify our calculations.
Each party chooses a private integer. As a numerical example, Alice chooses a = 13, and Bob chooses b = 15. Each of these values represents a private key and must not be disclosed.
It is time for each party to calculate their public key using their private key from step 2 and the agreed-upon public variables from step 1. Alice calculates A = ga mod p = 313 mod 29 = 19 and Bob calculates B = gb mod p = 315 mod 29 = 26. These are the public keys.
Alice and Bob send the keys to each other. Bob receives A = ga mod p = 19, i.e., Alice’s public key. And Alice receives B = gb mod p = 26, i.e., Bob’s public key. This step is called the key exchange.
Alice and Bob can finally calculate the shared secret using the received public key and their own private key. Alice calculates Ba mod p = 2613 mod 29 = 10 and Bob calculates Ab mod p = 1915 mod 29 = 10. Both calculations yield the same result, gab mod p = 10, the shared secret key.
'''