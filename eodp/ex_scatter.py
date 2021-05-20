import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df = pd.read_csv('ex_prepdata.csv')
df.reset_index(inplace=True)
# use lmplot
sns.lmplot(x = "Income",
            y = "Offence count", 
            ci = None,
            data = df)
sns.scatterplot(data = df, x = "Income", y = "Offence count")
plt.title('Offence Count vs Income')
plt.show()

corr,_ = pearsonr(df["Income"], df["Offence count"])
print('Pearsons correlation: %.3f' % corr)