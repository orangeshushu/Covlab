import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/pearson.csv', index_col=0)

plt.figure(figsize=(10, 8))

ax = sns.heatmap(df, annot=True, cmap='coolwarm', center=0, linewidths=.5, annot_kws={"size": 11})

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=15)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=15)


plt.tight_layout()

plt.savefig("heatmap.jpg", dpi=300, format='jpg', bbox_inches='tight')
plt.show()
