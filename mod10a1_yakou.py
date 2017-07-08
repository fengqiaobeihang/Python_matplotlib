# -*- coding: utf-8 -*-
#画多条折线图
import numpy             as     np
import matplotlib.pyplot as     plt
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/test_albedo.xlsx')#open file
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
date      = sheet.col_values(0)[1:]#表示取第0-第365行
albedo    = sheet.col_values(1)[1:]
MOD10A1   = sheet.col_values(2)[1:] #col = sheet.col_values(0)##获取第一列的数据
####################################
fig   = plt.figure(figsize=(6,2.5))#设置图形界面的大小
ax    = fig.add_subplot(111)
######################################
ax.plot(date,albedo,  'b-o', label='January',   linewidth=1)
ax.plot(date,MOD10A1, 'c-D', label='February',  linewidth=1)
# ax.scatter(date,MOD10A1, marker='o', color='b', s=7)
# ax.plot(date,March,    'k-h', label='March',     linewidth=2)
# ax.plot(date,April,    'g-v', label='April',     linewidth=2,linestyle='--')
# ax.plot(date,September,'m-p', label='September', linewidth=2)
# ax.plot(date,October,  'r-s', label='October',   linewidth=2,linestyle='--')
# ax.plot(date,November, 'y-*', label='November',  linewidth=2)
# ax.plot(date,December, 'm-+', label='December',  linewidth=2,linestyle='--')
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
plt.grid(True,axis='y')#设置网格线
# ax.set_xticks([1, 2, 3, 4, 5])
# ax.set_xticklabels(['1637-2300','2300-3100','3100-3900','3900-4700','4700-5077']) 
# fig.autofmt_xdate()#旋转X轴标签
# ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15) 
############################################## 
ax.set_xlabel('Elevation(m)',fontproperties=font)
ax.set_ylabel('Wind speed(m/s)',fontproperties=font)
# plt.legend(numpoints=1)
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.63,1.01),ncol=4,fancybox=True,shadow=True,fontsize='7.5')
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext,fontproperties=font,fontsize='7.5')
# batt.plot()
plt.show()
# fig.savefig('Temperature.png',dpi=900)
print 'end'