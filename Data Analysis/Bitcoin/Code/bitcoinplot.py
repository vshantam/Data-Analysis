# This is just a demo code to plot values

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 

def load_data(path):
	return pd.read_csv(path, sep=",", engine="python", header=0, dialect=None)

path = '/root/bitcoin/BITCOINWATCH-MINING.csv'
df = load_data(path)

#handelling the mssing datas
df = df.bfill()

#handeling date format
dates = list(df.Date)
newdates = []
fmt=['r-','g-','b-']
for i in dates:
	newdates.append(mdates.strpdate2num('%Y-%m-%d')(i))

#plot variation

#x axis will be same because of dates y axis will be changing.
colname = 2#change the name.
plt.plot_date(x=newdates[:],y=df.iloc[:, colname][:],fmt=fmt[2])
plt.xlabel("Dates")
plt.ylabel("values")
plt.title("Bitcoin variations")
plt.grid(True)
plt.legend()
plt.show()



