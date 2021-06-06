import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()
data = pd.read_csv('president_heights.csv')
height = np.array(data['height(cm)'])
print(data.shape)
print("Mean of Heights = ",height.mean())
print("Standard Deviation of Height = ",height.std())
print("Minimum Height = ",np.min(height))
print("Maximum Height = ",np.max(height))

print("25th Percentile = ",np.percentile(height,25))
print("Median = ",np.median(height))
print("75th Percentile = ",np.percentile(height,75))

plt.hist(height)
plt.title("Height Distribution of president of USA")
plt.xlabel("Height(cm)")
plt.ylabel("Number")
plt.show()
