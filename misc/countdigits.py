# Replace ___ with your code
print("Enter a number : ")
number = int(input())

count = 0

# run loop as long as number != 0
while (number != 0):
    # divide number by 10
    number //= 10#use // operator for integer quotient
      
    # increase count by 1
    count += 1

# print count
print('The number of digits entered :: ', count)

