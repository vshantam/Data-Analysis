import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import quandl

def load_data(path):
	return pd.read_csv(path, sep=",", engine="python", header=0, dialect=None)

path = '/root/bitcoin/BITCOINWATCH-MINING.csv'
df = load_data(path)

#or using quandl api
quandl.ApiConfig.api_key ='8NCm_V55725o9WHs9wsb'use your own api key
df1 = quandl.get("BITCOINWATCH/MINING", authtoken="8NCm_V55725o9WHs9wsb")
#handelling the mssing datas
df = df.ffill()

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



