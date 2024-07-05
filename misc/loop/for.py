#for loop
import time

for i in range(10):
    print(i + 1)

for i in range(50, 101, 2):#first is inclusive, 2nd arguement is exclusive
    print(i)

for i in "Kath Mandu":
    print(i)#print each letter in string

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)#sleep for 1 sec

print("Happy New year!")