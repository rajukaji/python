import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.plot(bike_sharing['dteday'], bike_sharing['casual'])

plt.plot(bike_sharing['dteday'], bike_sharing['registered'])

plt.xticks(rotation=30)
plt.ylabel('Bikes Rented')

plt.xlabel('Date')

plt.title('Bikes Rented: Casual vs. Registered')

plt.legend(['Casual', 'Registered'])

plt.show()