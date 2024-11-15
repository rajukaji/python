import pandas as pd
# housing = pd.read_csv('housing.csv')
import seaborn as sns
# is standard form
# seaborn uses matplotlib.pyplot library
import matplotlib.pyplot as plt

sns.set_theme()
# sets seaborn theme

sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice', hue='Overall Qual', palette='RdYlGn', size='Garage Area', sizes=(1, 300), col='Year')
plt.show()