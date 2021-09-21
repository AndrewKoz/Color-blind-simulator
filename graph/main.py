import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#line_zero = [[0, 0, 100, 100, 0], [0, 100, 100, 0, 0]]
#line_one = [[55, 45, 45, 45, 35, 35, 25, 25, 25, 15, 15], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
#line_two = [[75, 75, 65, 65, 55, 55, 55, 45, 45, 45, 35], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
#line_three = [[95, 95, 85, 85, 85, 75, 75, 75, 65, 65, 55], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]

fig, ax = plt.subplots()

plt.plot([0, 0, 100, 100, 0], [0, 100, 100, 0, 0], color='black')
plt.plot([55, 45, 45, 45, 35, 35, 25, 25, 25, 15, 15], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], color='black')
plt.plot([75, 75, 65, 65, 55, 55, 55, 45, 45, 45, 35], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], color='black')
plt.plot([95, 95, 85, 85, 85, 75, 75, 75, 65, 65, 55], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], color='black')
plt.fill_betweenx([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                  [55, 45, 45, 45, 35, 35, 25, 25, 25, 15, 15], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  color='red', label='Оценка 2')
plt.fill_betweenx([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                  [55, 45, 45, 45, 35, 35, 25, 25, 25, 15, 15], [75, 75, 65, 65, 55, 55, 55, 45, 45, 45, 35],
                  color='orange', label='Оценка 3')
plt.fill_betweenx([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                  [75, 75, 65, 65, 55, 55, 55, 45, 45, 45, 35], [95, 95, 85, 85, 85, 75, 75, 75, 65, 65, 55],
                  color='green', label='Оценка 4')
plt.fill_betweenx([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                  [95, 95, 85, 85, 85, 75, 75, 75, 65, 65, 55], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                  color='purple', label='Оценка 5')
ax.grid()
ax.set_xlabel('Выполнен зачёт (%)')
ax.set_ylabel('Выполнено ДЗ (%)')
fig.set_figwidth(12)
fig.set_figheight(10)

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))


ax.legend(fontsize=12,
          ncol=2,
          facecolor='oldlace',
          edgecolor='red',
          loc="lower left")

plt.show()
