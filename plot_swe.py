# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/1637SWE.xlsx')
# read seperate data
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
ASMR1   = sheet.col_values(0)[1:]#表示取第0-第365行
MODEL1  = sheet.col_values(1)[1:]
# ASMR2   = sheet.col_values(3)[1:]
# MODEL2  = sheet.col_values(4)[1:]
# ASMR3   = sheet.col_values(6)[1:]
# MODEL3  = sheet.col_values(7)[1:]
# ASMR4   = sheet.col_values(9)[1:]
# MODEL4  = sheet.col_values(10)[1:]
# ASMR5   = sheet.col_values(12)[1:]
# MODEL5  = sheet.col_values(13)[1:]
#########################################
fig         = plt.figure(figsize=(4,4))#设置图形界面的大小
ax          = fig.add_subplot(111)
#########################################
plt.scatter(ASMR1, MODEL1, marker='o', color='b', s=20)
lx1=np.linspace(-40,100,5)
ly1=lx1
plt.plot(lx1,ly1,linewidth=1.0,color='r')
plt.xlim(0,55)
plt.ylim(0,55)
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

font = matplotlib.font_manager.FontProperties(family='times new roman',size=12)  
#########################################
plt.xlabel('AMSR-E',fontproperties=font)#fontproperties=font
plt.ylabel('Simulation',  fontproperties=font)
##############################################
plt.legend()
# batt.plot()
plt.show()
fig.savefig('SWE4700.jpg',dpi=600)
print 'end'