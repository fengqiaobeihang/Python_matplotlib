# -*- coding: utf-8 -*-
#画多条折线图
import numpy             as     np
import matplotlib.pyplot as     plt
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data     = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/BLOWING.xlsx')#open file
sheet    = data.sheets()[0] #Select table (which tables are shown in brackets)
# Generate fake data
date     = sheet.col_values(0)
BLOWING  = sheet.col_values(1)#[0:365]#表示取第0-第365行
####################################
fig      = plt.figure(figsize=(7,3))#设置图形界面的大小
ax       = fig.add_subplot(111)
ax.bar(date,BLOWING,width = 0.35)
# ######################################
ax.set_xlim(0,52686)#X轴的数值范围
# #修改X轴的字体大小
# for xtick in ax.xaxis.get_major_ticks():
# 	xtick.label1.set_fontsize(12)
# #修改Y轴的字体大小
# for ytick in ax.yaxis.get_major_ticks():
# 	ytick.label1.set_fontsize(12)
# plt.legend(loc='upper right')#图例
plt.grid(True,axis='y')#设置网格线
ax.set_xticks([2096, 6560, 10592, 15056, 19502, 23966, 28286, 32750, 37214, 41534,45998,50318])
ax.set_xticklabels(['2014.1','2014.2','2014.3','2014.4','2014.5','2014.6','2014.7','2014.8','2014.9','2014.10','2014.11','2014.12']) 
fig.autofmt_xdate()#旋转X轴标签
# # ax.set_xlabel('Hydrological years')
font = matplotlib.font_manager.FontProperties(family='times new roman',size=15)  
ax.set_xlabel('Date',fontproperties=font)
ax.set_ylabel('Blowing snow$(g/m^2s)$',fontproperties=font)
# ##############################################
# # plt.legend(numpoints=1)
# plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.74,1.00),ncol=3,fancybox=True,shadow=True)
# leg = plt.gca().get_legend()
# ltext  = leg.get_texts()
# plt.setp(ltext,fontproperties=font)
# batt.plot()
plt.show()
# fig.savefig('blowing.png',dpi=900)
print 'end'