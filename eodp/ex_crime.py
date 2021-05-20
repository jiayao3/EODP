import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
import numpy as np

df = pd.read_csv('combine.csv')
df['date'] = pd.to_datetime(df['Reported Date'])
df['year'] = df['date'].dt.year
df = df.groupby(by = ['Offence Level 2 Description', 'year']).agg({'Offence count':sum})
df.reset_index(inplace=True)
df = df.set_index('Offence Level 2 Description')
# "PROPERTY DAMAGE AND ENVIRONMENTAL", "SERIOUS CRIMINAL TRESPASS","HOMICIDE AND RELATED OFFENCES", "OTHER OFFENCES AGAINST THE PERSON"ACTS INTENDED TO CAUSE INJURY，"ACTS INTENDED TO CAUSE INJURY","SEXUAL ASSAULT AND RELATED OFFENCES","FRAUD DECEPTION AND RELATED OFFENCES"
df = df.drop(["THEFT AND RELATED OFFENCES"])
df.reset_index(inplace=True)
df.to_csv("ex_crimetypedata.csv")
print(df)
