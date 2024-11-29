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

plt.show()
