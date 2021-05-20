import pandas as pd
import matplotlib.pyplot as plot
from numpy import arange

df = pd.read_csv('combine.csv')
df['date'] = pd.to_datetime(df['Reported Date'])
df['year'] = df['date'].dt.year
df = df.groupby(by = ['Offence Level 2 Description']).agg({'Offence count':sum})
df.reset_index(inplace=True)


plot.figure(figsize=(7,5))
off = df['Offence Level 2 Description'].tolist()
count = df['Offence count'].tolist()
plot.title('Offence Count')
plot.xlabel('Offence Type')
plot.ylabel('Number of Offence')
plot.bar(arange(len(count)),count)
plot.xticks( arange(len(off)),off, rotation=15)
plot.xticks(size = 5)
plot.show(block=True)