# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

yakouwindspeed = np.loadtxt('TEST1.txt')
plt.plot(yakouwindspeed)
plt.show()
meteodata_index=[
"TIMESTAMP",
"RainSnowacc",
"RainSnow",
"Snow_Depth",
"Soil_T_0_Avg",
"Soil_T_4_Avg",
"Soil_T_10_Avg",
"Soil_T_20_Avg",
"Soil_T_40_Avg",
"Soil_T_80_Avg",
"Soil_T_120_Avg",
"Soil_T_160_Avg",
"Soil_M_4_Avg",
"Soil_M_10_Avg",
"Soil_M_20_Avg",
"Soil_M_40_Avg",
"Soil_M_80_Avg",
"Soil_M_120_Avg",
"Soil_M_160_Avg",
"shf_Avg_1",
"shf_Avg_2",
"PTemp_Avg",
"short_up_Avg",
"short_dn_Avg",
"long_up_corr_Avg",
"long_dn_corr_Avg",
"Rn_Avg",
"albedo_Avg",
"cnr4_T_C_Avg",
"TargTemp_Avg",
"WindDirect_deg",
"WindSpeed_Avg",
"AirTemp_C_Avg",
"RH_Avg",
"Barometer_KPa_Avg",
"Rain_mm_Avg",
"PTemp",
"batt_volt"
]
meteodata   = pd.read_csv('meteo2014.csv', index_col=0,names =meteodata_index,parse_dates=True,skiprows=3)
# read seperate data
daily_meteo = meteodata.resample('D')
batt        = daily_meteo['WindSpeed_Avg']
fig         = plt.figure(figsize=(6,5))#设置图形界面的大小
ax          = fig.add_subplot(111)
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(10)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(10)
# plt.plot(batt)
fig.autofmt_xdate()#旋转X轴标签
plt.plot(batt,label='observation',color='b')
plt.plot(yakouwindspeed,label='WRF',color='r')
# plt.plot(yakoutemp-273.15,label='WRF',color='r')
ax.set_xlim(0,366)#X轴的数值范围
ax.set_xticks([16, 46, 76, 106, 136, 166, 196, 226, 256, 286, 316, 346])
ax.set_xticklabels(['2014.1','2014.2','2014.3','2014.4','2014.5','2014.6','2014.7','2014.8','2014.9','2014.10','2014.11','2014.12']) 
plt.xlabel('Date')
plt.ylabel('Wind Speed(m/s)')
# plt.legend()
# batt.plot()
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='small')
plt.show()
fig.savefig('2014windspeed_pro.png',dpi=900)
print 'end'