# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

meteodata_index=[
"date",
"IMS",
"MOD-SSMI",
"MOD-B",
"TAI",
"I-TAI",
"average"
]
meteodata = pd.read_csv('snowcover2011.csv', index_col=0,names =meteodata_index,parse_dates=True,skiprows=1)
# read seperate data
daily_meteo = meteodata.resample('D')
####################################
IMS       = daily_meteo['IMS']
MOD_SSMI  = daily_meteo['MOD-SSMI']
MOD_B     = daily_meteo['MOD-B']
TAI       = daily_meteo['TAI']
I_TAI     = daily_meteo['I-TAI']
average   = daily_meteo['average']
####################################
# ts=pd.Series(IMS,index=pd.date_range('2/24/2004',periods=3944))
# ts=ts.cumsum()
# ts.plot()
fig   = plt.figure(figsize=(13,5))#设置图形界面的大小
ax    = fig.add_subplot(111)
ax.plot(IMS,     label='IMS',     color='b',linewidth=1.5)
ax.plot(MOD_SSMI,label='MOD-SSMI',color='c',linewidth=1.5,linestyle='--')
ax.plot(MOD_B,   label='MOD-B',   color='k',linewidth=1.5)
ax.plot(TAI,     label='TAI',     color='g',linewidth=1.5,linestyle='--')
ax.plot(I_TAI,   label='I-TAI',   color='m',linewidth=1.5)
ax.plot(average, label='Average', color='r',linewidth=1.5)
######################################
ax.set_ylim(0,2200000)#Y轴的数值范围
ax.set_xlim(0,365)#X轴的数值范围
ax = plt.gca()  # 获取当前图像的坐标轴信息
ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)
plt.legend(loc='upper right')#图例
plt.grid(True,axis='y')#设置网格线
# plt.plot(yakoutemp-273.15,label='WRF',color='r')
# ax.set_ylim(0,2500000)
# ax.set_xticks([2, 313, 674, 1039, 1403,1767,2131,2495,2859,3223,3584,3945])
# ax.set_xticklabels(['2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']) 

# ax.set_xticks([2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 122, 134])
# ax.set_xticklabels(['2004.2','2005.1','2006.1','2007.1','2008.1','2009.1','2010.1','2011.1','2012.1','2013.1','2014.1','2015.1']) 
# fig.autofmt_xdate()#旋转X轴标签

ax.set_xticks([16, 46, 76, 106, 136, 166, 196, 226, 256, 286, 316, 346])
ax.set_xticklabels(['2011.1','2011.2','2011.3','2011.4','2011.5','2011.6','2011.7','2011.8','2011.9','2011.10','2011.11','2011.12']) 
fig.autofmt_xdate()#旋转X轴标签

# ax.set_xticks([75, 167, 259, 349, 381, 440, 532, 624, 715])
# ax.set_xticklabels(['2007.3','2007.6','2007.9','2007.12','2008.1','2008.3','2008.6','2008.9','2008.12']) 
# fig.autofmt_xdate()#旋转X轴标签
xminorLocator = MultipleLocator(4) 
ax.xaxis.set_minor_locator(xminorLocator)
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
ax.set_xlabel('Date',fontproperties=font)
ax.set_ylabel('Snow Cover Area$(km^2)$',fontproperties=font)
##############################################
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.74,1.00),ncol=3,fancybox=True,shadow=True)
#上面bbox_to_anchor被赋予的二元组中，第一个数值用于控制legend的左右移动，值越大越向右边移动.
#第二个数值用于控制legend的上下移动，值越大，越向上移动。
# plt.legend(loc=1, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext,fontproperties=font)
# batt.plot()
plt.show()
fig.savefig('2011.png',dpi=900)
print 'end'