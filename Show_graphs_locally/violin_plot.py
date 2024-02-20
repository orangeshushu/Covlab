import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_dict = {
    "2020": [],
    "2021": [],
    "2022": [],
    "2023": []
}
df = []
print(len(data_dict["2020"]))
print(len(data_dict["2021"]))
print(len(data_dict["2022"]))
print(len(data_dict["2023"]))
for year, values in data_dict.items():
    for value in values:
        df.append({"Year": year, "Value": value})

df = pd.DataFrame(df)

plt.figure(figsize=(14,10))
plt.xlabel('Year', fontsize=24, labelpad=20)
plt.ylabel('Value', fontsize=24, labelpad=20)
sns.violinplot(x="Year", y="Value", data=df)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title("Rehabilitation time in different years",  y=1.05, fontsize=24)

plt.savefig('violin_plot.jpg', dpi=1000, bbox_inches='tight')

plt.show()