import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    # Write your code here
    str_array = []
    
    # lets create a dictionary to learn frequency as well as calculate the percentage
    frequency_calculate = {}
    total_trades_length = len(customers)
    
    for trade in customers:
        if trade not in frequency_calculate:
            frequency_calculate[trade] = 1
        else:
            frequency_calculate[trade] += 1
            
    meet_the_threshold = []
    
    for key, value in frequency_calculate.items():
        frequency_calculate[key] = value / total_trades_length * 100
        # percentage calculate
        if frequency_calculate[key] >= 5:
            meet_the_threshold.append(key)
            
    return sorted(meet_the_threshold)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()