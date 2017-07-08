# -*- coding: utf-8 -*-
#画多条折线图
import numpy             as     np
import matplotlib.pyplot as     plt
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/2014snow_grain.xlsx')#open file
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
cm = plt.cm.get_cmap('RdYlBu')  
# Generate fake data
date = sheet.col_values(0)[1:]#表示取第0-第365行
R2   = sheet.col_values(1)[1:] #col = sheet.col_values(0)##获取第一列的数据
####################################
fig   = plt.figure(figsize=(6,4))#设置图形界面的大小
ax    = fig.add_subplot(111)
######################################
ax.bar(date,R2,edgecolor = 'blue')
######################################
ax.set_ylim(0,300)#X轴的数值范围
ax.set_xlim(0,366)#X轴的数值范围
ax.set_xticks([16, 76, 166, 256, 346])
ax.set_xticklabels(['2014.1','2014.3','2014.6','2014.9','2014.12']) 
# ax.set_xticks([16, 46, 76, 106, 136, 166, 196, 226, 256, 286, 316, 346])
# ax.set_xticklabels(['2014.1','2014.2','2014.3','2014.4','2014.5','2014.6','2014.7','2014.8','2014.9','2014.10','2014.11','2014.12']) 
######################################
#修改X轴的字体大小
for xtick in ax.xaxis.get_major_ticks():
	xtick.label1.set_fontsize(12)
#修改Y轴的字体大小
for ytick in ax.yaxis.get_major_ticks():
	ytick.label1.set_fontsize(12)
plt.legend(loc='upper right')#图例
plt.grid(True,axis='y')#设置网格线
###################################
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15) 
############################################## 
ax.set_xlabel('Date', fontproperties=font)
ax.set_ylabel('Snow grain size($\mu$m)',fontproperties=font)
# ax.set_ylabel('Temperature Snow grain size($\mu$m)',fontproperties=font)
plt.show()
# fig.savefig('Snow grain size.png',dpi=900)
print 'end'