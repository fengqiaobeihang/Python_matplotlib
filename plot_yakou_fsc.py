# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

meteodata_index=[
"time",
"mod",
"obs",
]
meteodata = pd.read_csv('C:/Users/sdh/Desktop/hfsc.csv', index_col=0,names =meteodata_index,parse_dates=True,skiprows=1)
# read seperate data
daily_meteo = meteodata.resample('M')
####################################
mod       = daily_meteo['mod']
obs       = daily_meteo['obs']
####################################
# ts=pd.Series(IMS,index=pd.date_range('2/24/2004',periods=3944))
# ts=ts.cumsum()
# ts.plot()
fig   = plt.figure(figsize=(6,2.5))#设置图形界面的大小
ax    = fig.add_subplot(111)
ax.plot(mod,label='Simulation',color='b',linewidth=1.5)
ax.plot(obs,label='MODIS',     color='r',linewidth=1.5)
######################################
ax.set_ylim(0,1.0)#Y轴的数值范围
ax.set_xlim(0,85)#X轴的数值范围
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
################################################
fig.autofmt_xdate()#旋转X轴标签
ax.set_xticks([7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85])
ax.set_xticklabels(['2005.6','2005.12','2006.6','2006.12','2007.6','2007.12','2008.6','2008.12','2009.6','2009.12',\
	'2010.6','2010.12','2011.6','2011.12']) 
# xminorLocator = MultipleLocator(4) 
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
ax.set_xlabel('Date',fontproperties=font)
ax.set_ylabel('Fractional Snow Cover',fontproperties=font)
##############################################
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.83,1.00),ncol=3,fancybox=True,shadow=True)
#上面bbox_to_anchor被赋予的二元组中，第一个数值用于控制legend的左右移动，值越大越向右边移动.
#第二个数值用于控制legend的上下移动，值越大，越向上移动。
# plt.legend(loc=1, numpoints=1)
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='small',fontproperties=font)
# leg = plt.gca().get_legend()
# ltext  = leg.get_texts()
# plt.setp(ltext,fontproperties=font)
# batt.plot()
plt.show()
fig.savefig('2005-2011FSC(M).png',dpi=900)
print 'end'