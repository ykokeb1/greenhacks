# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 08:54:36 2021

@author: bgkem
"""
import pandas as pd
import matplotlib.pyplot as plt

# create data frames
df = pd.read_csv('RiskFactorData.csv')

acresBurnedPerAcres = df[['State','acresBurnedPerMillionAcresState']]
df_no_cali = acresBurnedPerAcres.drop(4)
#plt.hist(df_no_cali['acresBurnedPerMillionAcresState'],100)
#plt.xlabel("Acres burned per million acres in state")
#plt.ylabel("Count: Number of States")

sorted_acres = acresBurnedPerAcres.sort_values(by='acresBurnedPerMillionAcresState')

#Boundaries: 1000-7500
rf = 'acresBurnedPerMillionAcresState'
low_bound = 1000
high_bound = 7500
df_risk_levels = acresBurnedPerAcres.copy()
df_risk_levels.loc[df_risk_levels[rf] < low_bound, rf] = 1
df_risk_levels.loc[(df_risk_levels[rf] > low_bound) & (df_risk_levels[rf] <= high_bound), rf] = 2
df_risk_levels.loc[df_risk_levels[rf] > high_bound, rf] = 3

#L-M-H separated data frames
df_low = acresBurnedPerAcres[df_risk_levels[rf] == 1]
df_med = acresBurnedPerAcres[df_risk_levels[rf]== 2]
df_high = acresBurnedPerAcres[df_risk_levels[rf]==3]

#save to .csv file
#df_risk_levels.to_csv('risk_levels.csv')

plt.hist([df_low[rf],df_med[rf],df_high[rf]], 100,color=["green","orange","red"],histtype='barstacked')
plt.xlabel("Acres burned per million acres in state")
plt.ylabel("Count: Number of States")