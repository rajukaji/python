import pandas as pd
housing = pd.read_csv('housing.csv')
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
# sets seaborn theme

sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice')
plt.show()