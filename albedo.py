# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('H:/2016-6-8/albedo.xlsx')
# read seperate data
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
observation = sheet.col_values(1)[1:83]#表示取第0-第365行
ww_data     = sheet.col_values(2)[1:83]
#########################################
fig         = plt.figure(figsize=(6,5))#设置图形界面的大小
ax          = fig.add_subplot(111)
ax.set_xlim(0.5,1.0)#X轴的数值范围
ax.set_ylim(0.5,1.0)#y轴的数值范围
#########################################
# plt.plot(batt,label='observation',color='b')
# plt.plot(yakouwindspeed,label='WRF',color='r')
#########################################
plt.scatter(observation, ww_data, marker='o', color='b', s=20)
lx1=np.linspace(-40,20,5)
ly1=lx1
plt.plot(lx1,ly1,linewidth=1.0,color='k')
plt.xlim(0.6,1)
plt.ylim(0.6,1)
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
########################################
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)

font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
#########################################
plt.xlabel('Yakou Observation Albedo',fontproperties=font)
plt.ylabel('TARTES Model Albedo',   fontproperties=font)
##############################################
plt.legend()
# batt.plot()
plt.show()
# fig.savefig('TARTES Model Albedo.png',dpi=900)
print 'end'