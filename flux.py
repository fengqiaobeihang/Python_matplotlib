# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/flux_yakou.xlsx')
# read seperate data
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
down_flux   = sheet.col_values(1)#[0:365]#表示取第0-第365行
up_flux     = sheet.col_values(2)#[0:365]
#########################################
fig         = plt.figure(figsize=(5,4))#设置图形界面的大小
ax          = fig.add_subplot(111)
####################################
ax.plot(down_flux,  label='downward flux', color='b',linewidth=1.0)
ax.plot(up_flux,    label='upwelling  flux',   color='r',linewidth=1.0)
######################################
ax.set_ylim(0,1700)#Y轴的数值范围
# ax.set_xlim(0,315)#X轴的数值范围
# ax = plt.gca()  # 获取当前图像的坐标轴信息
# ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(8)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(8)
# plt.legend(loc='upper right')#图例
# plt.grid(True,axis='y')#设置网格线

ax.set_xticks([45, 100, 155, 210, 265,320])
ax.set_xticklabels(['April 4','April 10','April 15','April 20','April 25','April 30']) 
fig.autofmt_xdate()#旋转X轴标签
# xminorLocator = MultipleLocator(4) 
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=10)  
# ax.set_xlabel('Date',fontproperties=font)
ax.set_xlabel('Date',fontproperties=font)
ax.set_ylabel('Radiation Flux(W)',fontproperties=font)
##############################################
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.83,1.00),ncol=3,fancybox=True,shadow=True)
#上面bbox_to_anchor被赋予的二元组中，第一个数值用于控制legend的左右移动，值越大越向右边移动.
#第二个数值用于控制legend的上下移动，值越大，越向上移动。
# plt.legend(loc=1, numpoints=1)
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='small',fontproperties=font)
# batt.plot()
plt.show()
fig.savefig('Flux.jpg',dpi=600)
print 'end'