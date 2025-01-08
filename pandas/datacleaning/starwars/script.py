# https://github.com/fivethirtyeight/data/tree/master/star-wars-survey
# fivethrtyeight
# https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

star_wars = pd.read_csv(r'C:\Users\h9\Desktop\python\pandas\datacleaning\starwars\star_wars.csv', encoding='ISO-8859-1')
# print(star_wars.head())
print(star_wars.columns)

print(star_wars[star_wars.columns[15]])