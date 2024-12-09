weight = 41.5

# Ground Shipping

cost ='Ground Shipping Total Cost:'

if weight <= 2:
  print(cost, weight * 1.50 + 20.00)
elif weight <= 6:
  print(cost, weight * 3.00 + 20.00)
elif weight <= 10:
  print(cost, weight * 4.00 + 20.00)
elif weight > 10:
  print(cost, weight * 4.75 + 20.00)

ground_ship_premium_cost = 125

print('ground shipping premium:', ground_ship_premium_cost)
print('\n\n', '=='*15, '\n\n')

'''
What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
'''
# answer: 34.4$ for ground shipping
# answer: 43.19999999 for drone shipping, 
# hence, use ground shipping

'''
What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
'''
# answer: 217.125$ for ground shipping, but, premium 125
# answer: 591.375 for drone shipping, not good
# use ground shipping premium instead

# Drone Shipping

weight = 41.5

cost = 'Drone Shipping Total Cost:'

if weight <= 2:
  print(cost, weight * 4.50)
elif weight <= 6:
  print(cost, weight * 9.00)
elif weight <= 10:
  print(cost, weight * 12.00)
elif weight > 10:
  print(cost, weight * 14.25)

print('\n\n', '=='*15, '\n\n')
