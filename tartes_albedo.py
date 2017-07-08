# -*- coding: utf-8 -*-
#画多条折线图
import numpy             as     np
import matplotlib.pyplot as     plt
import xlrd
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter
from   matplotlib.pylab  import *

data  = xlrd.open_workbook('C:/Users/sdh/Desktop/WRF_verify/bc_albedo.xlsx')#open file
sheet = data.sheets()[0] #Select table (which tables are shown in brackets)
cm = plt.cm.get_cmap('RdYlBu')  
# Generate fake data
wavelength = sheet.col_values(0)[1:]#表示取第0-第365行
diam1      = sheet.col_values(1)[1:] #col = sheet.col_values(0)##获取第一列的数据
diam2      = sheet.col_values(2)[1:] #row = sheet.row_values(0)##获取第一行的数据
diam3      = sheet.col_values(3)[1:]
diam4      = sheet.col_values(4)[1:]
diam5      = sheet.col_values(5)[1:]
diam6      = sheet.col_values(6)[1:]
diam7      = sheet.col_values(7)[1:]
diam8      = sheet.col_values(8)[1:]
diam9      = sheet.col_values(9)[1:]
####################################
fig   = plt.figure(figsize=(6,4))#设置图形界面的大小
ax    = fig.add_subplot(111)
######################################
ax.plot(wavelength, diam1, label='0.1mm',  linewidth=1)
ax.plot(wavelength, diam2, label='0.2mm',  linewidth=1)
ax.plot(wavelength, diam3, label='0.3mm',  linewidth=1)
ax.plot(wavelength, diam4, label='0.4mm',  linewidth=1)
ax.plot(wavelength, diam5, label='0.5mm',  linewidth=1)
ax.plot(wavelength, diam6, label='0.6mm',  linewidth=1)
ax.plot(wavelength, diam7, label='0.7mm',  linewidth=1)
ax.plot(wavelength, diam8, label='0.8mm',  linewidth=1)
ax.plot(wavelength, diam9, label='0.9mm',  linewidth=1)
######################################
ax.set_xlim(300,2500)#X轴的数值范围
# ax = plt.gca()  # 获取当前图像的坐标轴信息
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
ax.set_xlabel('Wavelength/nm',fontproperties=font)
ax.set_ylabel('Albedo',       fontproperties=font)
##############################################
# plt.legend(numpoints=1)
plt.legend(loc='upper center',numpoints=1,bbox_to_anchor=(0.75,1.0),ncol=3,fancybox=True,shadow=True,fontsize='7.5')
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext,fontproperties=font,fontsize='7.5')
# batt.plot()
plt.show()
fig.savefig('tartes_bc_albedo.png',dpi=900)
print 'end'