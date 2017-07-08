# -*- coding: utf-8 -*-
#画多条折线图
import numpy             as     np
import matplotlib.pyplot as     plt
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/snow.xlsx')#open file
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
date   = sheet.col_values(0)#[0:365]#表示取第0-第365行
T2000  = sheet.col_values(1)#[0:365] #col = sheet.col_values(0)##获取第一列的数据
T2001  = sheet.col_values(2)#[0:365] #row = sheet.row_values(0)##获取第一行的数据
T2002  = sheet.col_values(3)#[0:365]
T2003  = sheet.col_values(4)#[0:365]
T2004  = sheet.col_values(5)#[0:365]
T2005  = sheet.col_values(6)#[0:365]
T2006  = sheet.col_values(7)#[0:365]
T2007  = sheet.col_values(8)#[0:365]
T2008  = sheet.col_values(9)#[0:365]
T2009  = sheet.col_values(10)#[0:365]
T2010  = sheet.col_values(11)#[0:365]
T2011  = sheet.col_values(12)#[0:365]
T2012  = sheet.col_values(13)#[0:365]
####################################
fig   = plt.figure(figsize=(6,2.5))#设置图形界面的大小
ax    = fig.add_subplot(111)
# ax.scatter(date,IMS,     marker='H', color='b', s=20)
# ax.scatter(date,MOD_SSMI,marker='H', color='c', s=20)
# ax.scatter(date,MOD_B,   marker='H', color='k', s=20)
# ax.scatter(date,TAI,     marker='H', color='g', s=20)
# ax.scatter(date,I_TAI,   marker='H', color='y', s=20)
# ax.scatter(date,average, marker='H', color='r', s=20)
# a=plot.color('#eeefff')
######################################
ax.plot(date,T2000, 'b-o', label='2000',  linewidth=1.0)
ax.plot(date,T2001, 'c-D', label='2001',  linewidth=1.0,linestyle='--')
ax.plot(date,T2002, 'k-h', label='2002',  linewidth=1.0)
ax.plot(date,T2003, 'g-v', label='2003',  linewidth=1.0,linestyle='--')
ax.plot(date,T2004, 'm-p', label='2004',  linewidth=1.0)
ax.plot(date,T2005, 'r-s', label='2005',  linewidth=1.0,linestyle='--')
ax.plot(date,T2006, 'y-*', label='2006',  linewidth=1.0)
ax.plot(date,T2007, 'm-+', label='2007',  linewidth=1.0,linestyle='--')
ax.plot(date,T2008, 'c-o', label='2008',  linewidth=1.0)
ax.plot(date,T2009, 'b-D', label='2009',  linewidth=1.0,linestyle='--')
ax.plot(date,T2010, 'g-h', label='2010',  linewidth=1.0)
ax.plot(date,T2011, 'k-v', label='2011',  linewidth=1.0,linestyle='--')
ax.plot(date,T2012, 'r-p', label='2012',  linewidth=1.0)
######################################
# ax.plot(date,January,  'o', label='January',   linewidth=2,linestyle='-')
# ax.plot(date,February, 'D', label='February',  linewidth=2,linestyle='--')
# ax.plot(date,March,    'h', label='March',     linewidth=2,linestyle='-')
# ax.plot(date,April,    'v', label='April',     linewidth=2,linestyle='-')
# ax.plot(date,September,'p', label='September', linewidth=2,linestyle='--')
# ax.plot(date,October,  's', label='October',   linewidth=2,linestyle='-')
# ax.plot(date,November, '*', label='November',  linewidth=2,linestyle='--')
# ax.plot(date,December, '+', label='December',  linewidth=2,linestyle='-')
######################################
# ax.set_ylim(0,10)#Y轴的数值范围
ax = plt.gca()  # 获取当前图像的坐标轴信息
# ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
######################################
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)
plt.legend(loc='upper right')#图例
# plt.grid(True,axis='y')#设置网格线
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(['1637-2300','2300-3100','3100-3900','3900-4700','4700-5077']) 
# fig.autofmt_xdate()#旋转X轴标签
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15) 
############################################## 
ax.set_xlabel('Elevation(m)',fontproperties=font)
# ax.set_ylabel('Wind speed(m/s)',fontproperties=font)
##############################################
# ax.set_xlabel('Elevation(m)',fontproperties=font)
# ax.set_ylabel('Precipitation(mm)',fontproperties=font)
##############################################
# ax.set_xlabel('Elevation(m)',fontproperties=font)
# ax.set_ylabel('Temperature ($^\circ$C)',fontproperties=font)
# ax.set_ylabel('Snowmelt Runoff',fontproperties=font)
ax.set_ylabel('Snowfall',fontproperties=font)
##############################################
# plt.legend(numpoints=1)
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.705,1.01),ncol=4,fancybox=True,shadow=True,fontsize='7.5')
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext,fontproperties=font,fontsize='7.5')
# batt.plot()
plt.show()
fig.savefig('snow.png',dpi=600)
print 'end'