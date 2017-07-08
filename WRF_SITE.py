# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

meteodata_index=[
"TIMESTAMP",
"sunan",
"yeniugou",
"qilian",
"yeniugoucorrect",
"sunancorrect",
"qiliancorrect"
]
sitedata = pd.read_csv('I:/data/2007site_ws_daily.csv', index_col=0,names =meteodata_index,parse_dates=True,skiprows=1)
# read seperate data
WRF_meteo = sitedata.resample('D')
WRF = WRF_meteo['qilian']
WRF_SUNAN = WRF_meteo['sunan']
#######################################################
observationdata_index=[
"timedata",
"sunanobservation",
"yeniugouobservation",
"qilianobservation"
]
observationdata = pd.read_csv('I:/data/2007observation.csv', index_col=0,names =observationdata_index,parse_dates=True,skiprows=1)
# read seperate data
observation_meteo = observationdata.resample('D')
observation = observation_meteo['qilianobservation']
observation_sunan = observation_meteo['sunanobservation']
#######################################################
fig         = plt.figure(figsize=(6,10))#设置图形界面的大小
ax          = fig.add_subplot(111)
ax.set_xlim(0,366)#X轴的数值范围
##################################################
plt.subplot(411)
# ax.set_title('2007-Qilian')
# plt.title('2007-Qilian')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15) 
plt.plot(WRF,label='Qilian_WRF',color='b',linewidth=1.0)#Yeniugou Qilian Sunan
plt.plot(observation,label='Qilian_Observation',color='r',linewidth=1.0)
plt.ylabel('Wind Speed(m/s)',fontproperties=font)
plt.xlabel('2007-Qilian',fontproperties=font)
######################################################################## 
################################################
# plt.title('2007-Sunan')
ax.set_xlim(0,366)
plt.subplot(412)
plt.plot(WRF_SUNAN,label='WRF_SUNAN',color='b',linewidth=1.0)#Yeniugou Qilian Sunan
plt.plot(observation_sunan,label='observation_sunan',color='r',linewidth=1.0)
plt.ylabel('Wind Speed(m/s)',fontproperties=font)
plt.xlabel('2007-Sunan',fontproperties=font)
# plt.xlabel('Date(month)',fontproperties=font)
# plt.ylabel('Wind Speed(m/s)',fontproperties=font)
# plt.ylabel('Temperature ($^\circ$C)')
##############################################
meteodata_index2008=[
"TIMESTAMP",
"sunan",
"yeniugou",
"qilian",
"yeniugoucorrect",
"sunancorrect",
"qiliancorrect"
]
sitedata2008 = pd.read_csv('I:/data/2008site_ws_daily.csv', index_col=0,names =meteodata_index2008,parse_dates=True,skiprows=1)
# read seperate data
WRF_meteo2008 = sitedata2008.resample('D')
WRF2008 = WRF_meteo2008['qilian']
WRF_SUNAN2008 = WRF_meteo2008['sunan']
#######################################################
observationdata_index2008=[
"timedata",
"sunanobservation",
"yeniugouobservation",
"qilianobservation"
]
observationdata2008 = pd.read_csv('I:/data/2008observation.csv', index_col=0,names =observationdata_index2008,parse_dates=True,skiprows=1)
# read seperate data
observation_meteo2008 = observationdata2008.resample('D')
observation2008 = observation_meteo2008['qilianobservation']
observation_sunan2008 = observation_meteo2008['sunanobservation']
#######################################################
plt.subplot(413)
# ax.set_title('2007-Qilian')
# plt.title('2007-Qilian')
ax.set_xlim(0,366)
plt.plot(WRF2008,label='Qilian_WRF',color='b',linewidth=1.0)#Yeniugou Qilian Sunan
plt.plot(observation2008,label='Qilian_Observation',color='r',linewidth=1.0)
plt.ylabel('Wind Speed(m/s)',fontproperties=font)
plt.xlabel('2008-Qilian',fontproperties=font)
########################################################################
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
################################################
# plt.title('2008-Sunan')
plt.subplot(414)
ax.set_xlim(0,366)
plt.plot(WRF_SUNAN2008,label='WRF_SUNAN',color='b',linewidth=1.0)#Yeniugou Qilian Sunan
plt.plot(observation_sunan2008,label='observation_sunan',color='r',linewidth=1.0)
##############################################
plt.xlabel('2008-Sunan',fontproperties=font)
# plt.xlabel('Date',fontproperties=font)
plt.ylabel('Wind Speed(m/s)',fontproperties=font)
# plt.legend()
# fig.savefig('I:/atmosphere_data/windspeed.jpg',dpi=900)
plt.show()
print 'end'