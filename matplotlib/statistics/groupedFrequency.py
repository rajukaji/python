import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

registered_freq = bike_sharing['registered'].value_counts(bins=10).sort_index()

casual_freq = bike_sharing['casual'].value_counts(bins=10).sort_index()