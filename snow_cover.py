# -*- coding: utf-8 -*-
import pandas as pd
import numpy             as np
import xlrd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from   matplotlib.pylab  import *
from   matplotlib.colors import *
from   scipy.stats       import gaussian_kde
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/snow/rh4.xlsx')
sheet = data.sheets()[0]
# Generate fake data
x = sheet.col_values(0)[0:]
y = sheet.col_values(1)[0:]
fig = plt.figure(figsize=(5,4))#设置图形界面的大小
ax  = fig.add_subplot(111)
# Calculate the point density
xy  = np.vstack([x,y])
z   = gaussian_kde(xy)(xy)
cm  = plt.cm.get_cmap('jet')#jet
fig1 = plt.scatter(x, y, c=z, s=20,marker='o', edgecolor='',cmap=cm)
plt.colorbar(fig1)   
ax  = plt.gca()
ax.set_ylim(0,100)#Y轴的数值范围
ax.set_xlim(35,)#Y轴的数值范围
#########################################
# xmajorLocator   = MultipleLocator(0.1) #将x主刻度标签设置为20的倍数
# xminorLocator   = MultipleLocator(0.1) #将x轴次刻度标签设置为5的倍数
# ymajorLocator   = MultipleLocator(0.1) #将y主刻度标签设置为20的倍数
# yminorLocator   = MultipleLocator(0.1) #将y轴次刻度标签设置为5的倍数
# # ax.xaxis.set_major_locator(xmajorLocator)
# ax.yaxis.set_major_locator(ymajorLocator)
# #显示次刻度标签的位置,没有标签文本
# # ax.xaxis.set_minor_locator(xminorLocator)
# ax.yaxis.set_minor_locator(yminorLocator)
# #修改X轴的字体大小
# for xtick in ax.xaxis.get_major_ticks():
# 	xtick.label1.set_fontsize(12)
# #修改Y轴的字体大小
# for ytick in ax.yaxis.get_major_ticks():
# 	ytick.label1.set_fontsize(12)
font = matplotlib.font_manager.FontProperties(family='times new roman',size=12)  
#########################################Temperature  Relative Humidity precipitation
# plt.xlabel(u'海拔/m',fontproperties='SimHei')#fontproperties=font
# plt.ylabel(u'云下积雪反照率',  fontproperties='SimHei')
plt.xlabel('Relative Humidity(%)',fontproperties=font)#fontproperties=font
plt.ylabel('FSC(%)',  fontproperties=font)
##############################################
# ax.set_xlabel(u'海拔/m',fontproperties='SimHei')
# ax.set_ylabel(u'积雪反照率绝对误差',  fontproperties='SimHei')
plt.title('')
plt.show()
fig.savefig('R4.jpg',dpi=600)#relative error
print 'end'