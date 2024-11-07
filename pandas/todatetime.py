import pandas as pd

who_time_series = pd.read_csv('WHO_time_series.csv')

who_time_series['Date_reported'] = pd.to_datetime(who_time_series['Date_reported'])

print(who_time_series.head())
print(who_time_series.tail())
print(who_time_series.info())