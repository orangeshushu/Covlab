import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/reinfection_duration.csv')

data['Cumulative_Area'] = data['Frequency'].cumsum()

plt.figure(figsize=(14, 10))
plt.fill_between(data['Number'], data['Cumulative_Area'], color='skyblue', alpha=0.4)
plt.plot(data['Number'], data['Cumulative_Area'], color='skyblue', alpha=0.6)

plt.title('Time to reinfection', y=1.05, fontsize=27)
plt.tick_params(axis='both', which='major', labelsize=27)
plt.xlabel('Days between two self-reported positive tweets', labelpad=20, fontsize=27)
plt.ylabel('Proportion of cases', labelpad=20, fontsize=27)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('reinfections_days.jpg', dpi=1000, bbox_inches='tight')
plt.show()
