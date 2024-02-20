import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [238993, 17906, 3283, 1025, 1071]
y2 = [None, 7.49, 1.37, 0.43, 0.45]

fig, ax1 = plt.subplots(figsize=(14, 10))
plt.tick_params(axis='both', which='major', labelsize=18)

line1, = ax1.plot(x, y1, 'b-', label='Number of self-reported infections')
ax1.set_xlabel('Infection counts', labelpad=20, fontsize=24)
# ax1.set_ylabel('Self-reported infection user count', color='b', fontsize=20)
ax1.tick_params('y', colors='b', labelsize = 18)

for xi, yi in zip(x, y1):
    ax1.text(xi, yi - 10000, str(yi), color='blue', ha='center', va='bottom', fontsize=16)  

ax2 = ax1.twinx()
line2, = ax2.plot(x, y2, 'r-', label='Reinfection rate')
# ax2.set_ylabel('Infection rate(%)', color='r')
ax2.tick_params('y', colors='r', labelsize = 18)

for xi, yi in zip(x, y2):
    if yi is not None:
        ax2.text(xi, yi + 0.095, f"{yi:.2f}%", color='red', ha='left', fontsize =16)  

lines = [line1, line2]
ax1.legend(lines, [l.get_label() for l in lines], loc='upper right', fontsize=18)

ax1.set_xticks([1, 2, 3, 4, 5])
ax1.set_xticklabels(['1', '2', '3', '4', '>=5'])

# plt.tick_params(axis='both', which='major', labelsize=14)
plt.title("Infection counts and rates", y=1.05, fontsize=24)
plt.savefig('reinfection rate.jpg', dpi=1000, bbox_inches='tight')
plt.show()
