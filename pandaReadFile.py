import numpy as np;
import pandas as pd;

df = pd.read_csv(r'C:\Users\768940.CTS\Desktop\Python\pandas_tutorial_read.csv',
                 delimiter=";",names=['date_time', 'read_write','country','user_id', 'd_market','continent'])
#print(df)
print(df.shape)
#print(df[df['d_market']=="SEO"])
print(df.sample(5))
