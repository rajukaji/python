import math
#Smallest number divisible by first n numbers

n = 5

calc = [i for i in range(1, n+1)]

print(calc)
 
#print(math.lcm(calc))
first = calc[0]
value = 0
for i in calc:
    value = math.lcm(first, i)

print(value)

lcmm = 1
gcdd = 0
for i in range(1, 6):
    lcmm = math.lcm(1, i)
    gcdd = math.gcd(1, i)

print(lcmm, gcdd)

#Smallest number divisible by first n numbers

print(math.gcd(2, 4))

def smallest_multiple(n):
    import math
    ans = 1
    for i in range(1, n+1):
        ans = (ans * i) // math.gcd(ans, i)
    return ans
    # write your code here

# take integer input for n
n = int(input('enter a number  :: '))
# call the function
print(smallest_multiple(n))