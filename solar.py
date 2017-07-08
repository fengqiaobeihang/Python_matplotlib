# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('I:/snow albedo/coszen.xlsx')
# read seperate data
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
date      = sheet.col_values(0)#[0:365]#表示取第0-第365行
solar     = sheet.col_values(1)#[0:365]
#########################################
fig         = plt.figure(figsize=(5,4))#设置图形界面的大小
ax          = fig.add_subplot(111)
####################################
ax.plot(solar,  label='Solar Zenith Angle', color='b',linewidth=1.5)
######################################
# ax.set_ylim(0,2200000)#Y轴的数值范围
# ax.set_xlim(0,315)#X轴的数值范围
# ax = plt.gca()  # 获取当前图像的坐标轴信息
# ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)
# plt.legend(loc='upper right')#图例
plt.grid(True,axis='y')#设置网格线

ax.set_xticks([25, 73, 121, 169, 217])
ax.set_xticklabels(['April 2','April 4','April 6','April 8','April 10']) 
# fig.autofmt_xdate()#旋转X轴标签
# xminorLocator = MultipleLocator(4) 
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
# ax.set_xlabel('Date',fontproperties=font)
ax.set_xlabel('Date',fontproperties=font)
ax.set_ylabel('Solar Zenith Angle(degree)',fontproperties=font)
##############################################
# batt.plot()
plt.show()
fig.savefig('solar.jpg',dpi=600)
print 'end'