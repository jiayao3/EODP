import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('prepdata.csv')
df.reset_index(inplace=True)

sns.scatterplot(data = df, x = "Income", y = "Offence count")
plt.title('Offence Count vs Income (Before)')
plt.show()
