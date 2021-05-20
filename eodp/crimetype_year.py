import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
import numpy as np

df = pd.read_csv('combine.csv')
df['date'] = pd.to_datetime(df['Reported Date'])
df['year'] = df['date'].dt.year
df = df.groupby(by = ['Offence Level 2 Description', 'year']).agg({'Offence count':sum})
df.reset_index(inplace=True)

off = df['Offence Level 2 Description'].tolist()
count = df['Offence count'].tolist()
year = df['year'].tolist()

ls_off = []
type = []

for i in range(len(off)):
    if off[i] not in type:
        type.append(off[i])

for j in range(len(type)):
    ls_off.append([type[j]])
    for i in range(len(year)):
        if year[i] == 2012 and type[j]==off[i]:
            ls_off[j].append(count[i])
        elif year[i] == 2013 and type[j]==off[i]:
            ls_off[j].append(count[i])
        elif year[i] == 2014 and type[j]==off[i]:
            ls_off[j].append(count[i])
        elif year[i] == 2015 and type[j]==off[i]:
            ls_off[j].append(count[i])
        elif year[i] == 2016 and type[j]==off[i]:
            ls_off[j].append(count[i])
        elif year[i] == 2017 and type[j]==off[i]:
            ls_off[j].append(count[i])


df = pd.DataFrame([ls_off[0], ls_off[1], ls_off[2], ls_off[3], ls_off[4], ls_off[5], ls_off[6], ls_off[7],ls_off[8]],
                  columns=['Crime', '2012', '2013', '2014', '2015', '2016', '2017'])

print(df)

df.plot(x='Crime',
        kind='bar',
        stacked=False,
        title='Crime Counts for each Year')

plt.xlabel('Offence Type')
plt.ylabel('Number of Offence')
plt.xticks(size = 5, rotation=20)
plt.show()
df.to_csv("crimetypedata.csv")