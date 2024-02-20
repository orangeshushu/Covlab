import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# Create example recovery time data (in days)
recovery_times_2020 = np.array([])
recovery_times_2021 = np.array([])
recovery_times_2022 = np.array([])
recovery_times_2023 = np.array([])

print(len(recovery_times_2020))
print(len(recovery_times_2021))
print(len(recovery_times_2022))
print(len(recovery_times_2023))

# Create event status data (1 for recovery, 0 for not recovery)
event_status0 = np.ones([])
event_status1 = np.ones([])
event_status2 = np.ones([])
event_status3 = np.ones([])

# Create a DataFrame
data0 = pd.DataFrame({'recovery_time': recovery_times_2020, 'event': event_status0})
data1 = pd.DataFrame({'recovery_time': recovery_times_2021, 'event': event_status1})
data2 = pd.DataFrame({'recovery_time': recovery_times_2022, 'event': event_status2})
data3 = pd.DataFrame({'recovery_time': recovery_times_2023, 'event': event_status3})
# Initialize KaplanMeierFitter
kmf_0 = KaplanMeierFitter()
kmf_1 = KaplanMeierFitter()
kmf_2 = KaplanMeierFitter()
kmf_3 = KaplanMeierFitter()

# Fit the Kaplan-Meier cumulative density curve
kmf_0.fit(data0['recovery_time'], event_observed=data0['event'])
kmf_1.fit(data1['recovery_time'], event_observed=data1['event'])
kmf_2.fit(data2['recovery_time'], event_observed=data2['event'])
kmf_3.fit(data3['recovery_time'], event_observed=data3['event'])


# Increase font size for the graph
plt.rc('font', size=24)  # Set font size for x-axis labels
plt.rc('legend', fontsize=18)  # Set font size for legend

# Plot the cumulative density graph
plt.figure(figsize=(14, 10))
kmf_0.plot_cumulative_density(label='2020')
kmf_1.plot_cumulative_density(label='2021')
kmf_2.plot_cumulative_density(label='2022')
kmf_3.plot_cumulative_density(label='2023')

plt.xlabel('Recovery Time (Days)', labelpad=20)
plt.ylabel('Proportion Recovered', labelpad=20)
plt.title('Kaplan–Meier Estimates of Cumulative Recoveries', y=1.05, fontsize=24)

plt.savefig('cumulative_density.jpg', dpi=1000, bbox_inches='tight')

plt.legend()
plt.show()
