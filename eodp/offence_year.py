import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('combine.csv')
df['date'] = pd.to_datetime(df['Reported Date'])
df['year'] = df['date'].dt.year
df = df.groupby(by = ['year']).agg({'Offence count':sum})
df = df[2012:2017]
df.reset_index(inplace=True)
df.to_csv( "offdata.csv", index=False)

chart = df.plot.bar(x='year', y='Offence count', rot=0, title="Offence Count Per Year")
plot.show(block=True)

df = pd.read_csv('ex_crimetypedata.csv')
df = df.groupby(by = ['year']).agg({'Offence count':sum})
df = df[2012:2017]
df.reset_index(inplace=True)
df.to_csv( "ex_offdata.csv", index=False)