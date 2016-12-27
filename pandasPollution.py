import pandas as pd
from datetime import datetime
import pdb

df = pd.read_csv("pollution_us_2000_2016.csv")
def fmonth(x):
    return str(datetime.strptime(x, "%Y-%m-%d").month)
def fyear(x):
    return str(datetime.strptime(x, "%Y-%m-%d").year)
df['year'] = df['Date Local'].apply(fyear)
df2 = pd.groupby(df, by= [df['State'], df['year']]).mean()
df3 = pd.DataFrame(df2)
df3.to_csv("newstuff.csv")