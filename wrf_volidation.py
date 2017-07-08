# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data_wrf  = xlrd.open_workbook('I:/atmosphere_data/site_ws.xlsx')
# read seperate data
sheet_wrf = data_wrf.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
sunan_wrf      = sheet_wrf.col_values(3)[1:]#[0:365]#表示取第0-第365行
# yeniugou_wrf   = sheet_wrf.col_values(2)#[0:365]
# qilain_wrf     = sheet_wrf.col_values(3)
#########################################
data_observation  = xlrd.open_workbook('I:/atmosphere_data/observation.xlsx')
# read seperate data
sheet_observation = data_observation.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
sunan_observation      = sheet_observation.col_values(3)[1:]#[0:365]#表示取第0-第365行
# yeniugou_observation   = sheet_observation.col_values(2)#[0:365]
# qilain_observation     = sheet_observation.col_values(3)
#########################################
fig         = plt.figure(figsize=(15,5))#设置图形界面的大小
ax          = fig.add_subplot(111)
#########################################
# plt.scatter(sunan_observation, sunan_wrf, marker='o', color='b', s=80)
# lx1=np.linspace(-40,20,5)
# ly1=lx1
# plt.plot(lx1,ly1,linewidth=1.0,color='k')
# plt.xlim(0,1)
# plt.ylim(0,1)
plt.plot(sunan_wrf,label='Qilian_WRF',color='b')
plt.plot(sunan_observation,label='Qilian_Observation',color='r')
#########################################
# xmajorLocator   = MultipleLocator(0.1) #将x主刻度标签设置为20的倍数
# xminorLocator   = MultipleLocator(0.1) #将x轴次刻度标签设置为5的倍数
# ymajorLocator   = MultipleLocator(0.1) #将y主刻度标签设置为20的倍数
# yminorLocator   = MultipleLocator(0.1) #将y轴次刻度标签设置为5的倍数
# ax.xaxis.set_major_locator(xmajorLocator)
# ax.yaxis.set_major_locator(ymajorLocator)
# #显示次刻度标签的位置,没有标签文本
# ax.xaxis.set_minor_locator(xminorLocator)
# ax.yaxis.set_minor_locator(yminorLocator)
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)

font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
#########################################
plt.xlabel('Date',fontproperties=font)
plt.ylabel('Wind Speed(m/s)',fontproperties=font)
##############################################
plt.legend()
# batt.plot()
plt.show()
fig.savefig('2011-2014_Qilian.png',dpi=900)
print 'end'