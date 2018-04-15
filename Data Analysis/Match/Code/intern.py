# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:36:17 2018

@author: Shantam Vijayputra
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Match.csv")
x = df["Team_Name_Id"].reshape(-1,1)
z = df["Opponent_Team_Id"].reshape(-1,1)
y = df["Won_By"].reshape(-1,1)

fig = plt.figure()
bar1 = fig.add_subplot(111)
bar2 = fig.add_subplot(333)
bar1.set_xlabel("Team Name Id")
bar1.set_ylabel("Won By")
bar1.set_title("Winning Statistics")

#bar2.set_xlabel("Team Name Id")
#bar2.set_ylabel("Won By")
#bar2.set_title("      Winning Statistics")

bar1.bar(x-0.2 ,y,color = "green",linewidth = 2, label = "Team 1 ",align = "center")
bar2.bar(z,y,color = "red",linewidth=0.1,label = "Team 2",align = "center")
bar1.grid(True)
bar2.grid(True)
plt.gca()
bar1.legend((10,10))
bar2.legend((0,0))
plt.show()


plt.bar(df['Match_Winner_Id'],df['City_Name'],color = "orage",label = "Matches won")
plt.legend()

import plotly
 ct = pd.crosstab(df['City_Name'],df['Host_Country'])
plt.plot(ct['India'].values,ct['India'].index,color = "red",linewidth= 1, label = "India")
plt.plot(ct['U.A.E'].values,ct['U.A.E'].index,color = "green",linewidth = 2,label = "U.A.E")
plt.plot(ct['South Africa'].values,ct['South Africa'].index,linewidth = 3,color = "blue",label = "South Africa")
plt.legend()
plt.xlabel("Total matches played")
plt.ylabel("City")
plt.title("City vs Match played")
plt.show()

plt.pie([500,57,20], labels = ['India','South Africa','U.A.E'])

