import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('Standard_Income_Statement_2014-15.csv')
df = df.groupby(by = ['Year'][0:4]).agg({"Value ($'000)":sum})
df.reset_index(inplace=True)
df.columns = ['Year', 'Income']
def slice(x):
    return x[0:4]
df["Year"] = df["Year"].apply(slice)
income = list(df["Income"])
chart = df.plot.bar(x='Year', y='Income', rot=0, title="Income Per Year")
plot.show(block=True)

prep = pd.read_csv('ex_offdata.csv')
prep['Income'] = income
prep.to_csv( "ex_prepdata.csv")