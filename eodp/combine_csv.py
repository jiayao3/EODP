import pandas as pd
import csv

filenames = ["2011-12-data_sa_crime.csv","2012-13-data_sa_crime.csv","2013-14-data_sa_crime.csv",
    "2014-15-data_sa_crime.csv","2015-16-data_sa_crime.csv","2016-17-data_sa_crime.csv", "2017-18-data_sa_crime.csv"]
combined_csv = pd.concat([pd.read_csv(f) for f in filenames])

combined_csv.to_csv( "combine.csv", index=False)