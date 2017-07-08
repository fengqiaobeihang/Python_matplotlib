# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

meteodata_index=[
"TIME",
"STAMP",
"RH_Avg",
"Rain_mm_Avg"
]
meteodata = pd.read_csv('RH2.csv', index_col=0,names =meteodata_index,parse_dates=True,skiprows=3)
# read seperate data
daily_meteo = meteodata.resample('D')
####################################
RH2        = daily_meteo['RH_Avg']
precipation= daily_meteo['Rain_mm_Avg']
####################################
fig   = plt.figure(figsize=(6,2.5))#设置图形界面的大小
ax    = fig.add_subplot(111)
# ax.plot(RH2,     label='RH2',     color='b',linewidth=1.5)
ax.plot(precipation,  label='RH2', color='b',linewidth=1.5)
######################################
# ax.set_ylim(0,2200000)#Y轴的数值范围
ax.set_xlim(0,315)#X轴的数值范围
# ax = plt.gca()  # 获取当前图像的坐标轴信息
# ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)
# plt.legend(loc='upper right')#图例
# plt.grid(True,axis='y')#设置网格线

ax.set_xticks([15, 45, 75, 105, 135, 165, 195, 225, 255, 285,315])
ax.set_xticklabels(['2014.1','2014.2','2014.3','2014.4','2014.5','2014.6','2014.7','2014.8','2014.9','2014.10','2014.11']) 
fig.autofmt_xdate()#旋转X轴标签

# ax.set_xticks([75, 167, 259, 349, 381, 440, 532, 624, 715])
# ax.set_xticklabels(['2007.3','2007.6','2007.9','2007.12','2008.1','2008.3','2008.6','2008.9','2008.12']) 
# fig.autofmt_xdate()#旋转X轴标签
# xminorLocator = MultipleLocator(4) 
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
# ax.set_xlabel('Date',fontproperties=font)
ax.set_ylabel('Precipitation(mm)',fontproperties=font)
##############################################
# plt.legend()
#上面bbox_to_anchor被赋予的二元组中，第一个数值用于控制legend的左右移动，值越大越向右边移动.
#第二个数值用于控制legend的上下移动，值越大，越向上移动。
# plt.legend(loc=1, numpoints=1)
# leg = plt.gca().get_legend()
# ltext  = leg.get_texts()
# plt.setp(ltext,fontproperties=font)
# batt.plot()
plt.show()
# fig.savefig('Precipitation.png',dpi=600)
print 'end'