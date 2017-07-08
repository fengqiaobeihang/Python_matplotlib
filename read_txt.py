# -*- coding: utf-8 -*-
#shaodonghang
#2017-1-3
import locale
import codecs
import sys
import re
import math
import os
import os.path
import sys
from   os.path import walk
import linecache
import  numpy  as np

type=sys.getfilesystemencoding()
folderpath1="I:/atmosphere_data/LiHY/"
# folderpath2="C:/Users/dy/Desktop/data/data2/"
folderpath3="I:/atmosphere_data/result/qilian/"
for dirpath,filename,filenames in os.walk(folderpath1):
    for filename in filenames:
        if os.path.splitext(filename)[1]=='.TXT': #获取指定格式的文件,后缀名一定要对应大小写
            DEMfilepath   = os.path.join(dirpath,filename)
            # FSFilename    = filename.replace('u','v')
            RSFilename    = filename.replace('SURF_CLI_CHN_MUL_DAY-WIN-11002','wind-speed')
            # FSfilepath    = os.path.join(folderpath2,FSFilename)#合并绝对路径
            RESULTfilepath= os.path.join(folderpath3,RSFilename)

            savefile=codecs.open(RESULTfilepath,"w","utf-8")
            
            fDEMPointer= open(DEMfilepath,"r")
            # fFSPointer = open(FSfilepath,"r")
            nocls=linecache.getlines(DEMfilepath)
            rows =len(nocls)#文件的总行数
            print 'rows=',rows
            # print 'nocls=',nocls
            data=fDEMPointer.readlines()
            for line in data:
                wind=line.strip(' ').split()
                if wind[0]=='52657':
                    sunan=wind[7]
                    # np.savetxt('sca.txt',sunan+"\n")
                    savefile.writelines(sunan+"\n")

            # aa=['dfadf','dfasf\n','fsaf\n','dfasdf']
            # savefile.writelines(aa)
            savefile.close()
# fp=open("I:/atmosphere_data/result/wind-speed-200001.TXT")
# print(len(fp.readlines()))
print "done"