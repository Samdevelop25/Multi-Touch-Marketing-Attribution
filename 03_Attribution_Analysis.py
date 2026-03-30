import pandas as pd
import matplotlib.pyplot as plt

# Load data
traffic = pd.read_csv('../data/web_traffic.csv', parse_dates=['timestamp'])
conv = pd.read_csv('../data/conversions.csv', parse_dates=['conversion_time'])

# Merge to find the journey
df = pd.merge(traffic, conv, on='user_id')
df = df[df['timestamp'] <= df['conversion_time']]

# 1. First-Touch Attribution
first_touch = df.sort_values('timestamp').groupby('user_id').head(1)
ft_counts = first_touch['channel'].value_counts()

# 2. Last-Touch Attribution
last_touch = df.sort_values('timestamp').groupby('user_id').tail(1)
lt_counts = last_touch['channel'].value_counts()

# Plot Comparison
comparison = pd.DataFrame({'First Touch': ft_counts, 'Last Touch': lt_counts})
comparison.plot(kind='bar', figsize=(10, 6))
plt.title("Attribution Model Comparison: First vs Last Touch")
plt.ylabel("Attributed Conversions")
plt.show()
