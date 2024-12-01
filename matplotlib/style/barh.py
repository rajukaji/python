style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(9, 5))

# print(style.available)




# ax.barh()
ax.barh(white_corr.index, white_corr, left=2, height=0.5)
ax.barh(red_corr.index, red_corr, height=0.5)
ax.grid()
# remove all the gridlines, with visible=None default parameter

ax.set_xticks([])
ax.set_yticks([])
# remove both ticks



ax.barh(white_corr.index, white_corr, left=2, height=0.5)
ax.barh(red_corr.index, red_corr, height=0.5, left=-0.1)

ax.grid(False)
ax.set_yticklabels([])
ax.set_xticklabels([])

x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
            'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
            'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
            'Residual Sugar': 0.67, 'Citric Acid': 0.76,
            'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
y_coord = 9.8
for y_label, x_coord in x_coords.items():
    ax.text(x_coord, y_coord, y_label)
    y_coord -= 1
    

ax.axvline(x=0.5, color='grey', alpha=0.1, linewidth=1, ymin=0.1, ymax=0.9)
# add vertical lines


ax.axvline(x=1.45, color='grey', alpha=0.1, linewidth=1, ymin=0.1, ymax=0.9)


ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
          xmin=0.01, xmax=0.32)
ax.text(-0.7, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)
ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
           xmin=0.67, xmax=0.98)
ax.text(1.43, -1.7, '-0.5'+ ' '*31 + '+0.5',
        color='grey', alpha=0.5)
# horizontol line bottom


ax.axhline(y=11, color='grey', linewidth=1, alpha=0.5, xmin=0.01, xmax=0.32)
ax.text(x=-0.33, y=11.2, s='RED WINE', weight='bold')

ax.axhline(y=11, color='grey', linewidth=1, alpha=0.5, xmin=0.67, xmax=0.98)
ax.text(x=1.75, y=11.2, s='WHITE WINE', weight='bold')
# horizontal line top


ax.text(-0.7, -2.9,
        'DATAQUEST' + ' '*94 + 'Source: P. Cortez et al.',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
        fontsize=12)
# adding source

ax.text(s='Wine Quality Most Strongly Correlated With Alcohol Level', x=-0.7, y=13.5, fontsize=17, weight='bold')
ax.text(s='Correlation values between wine quality and wine properties (alcohol, pH, etc.)', x=-0.7, y=12.7)
# add title and subtitle

# using pandas
red_corr = red_wine.corr()['quality'][:-1]
postive_red = red_corr>=0
color_map_red = postive_red.map({True:'#33A1C9',
                                 False:'#ffae42'
                                })

ax.barh(red_corr.index, red_corr, color=color_map_red, height=0.8, left=-0.5)
# changing colors
# left negative correlation, right positive correlation

plt.show()