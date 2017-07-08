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

type=sys.getfilesystemencoding()

folderpath1="C:/Users/dy/Desktop/data/data1/"
folderpath2="C:/Users/dy/Desktop/data/data2/"
folderpath3="C:/Users/dy/Desktop/data/data3/"
for dirpath,filename,filenames in os.walk(folderpath1):
    for filename in filenames:
        if os.path.splitext(filename)[1]=='.txt': #获取指定格式的文件
            DEMfilepath   = os.path.join(dirpath,filename)
            # FSFilename    = filename.replace('u','v')
            # RSFilename    = filename.replace('u','r')
            FSfilepath    = os.path.join(folderpath2,FSFilename)#合并绝对路径
            RESULTfilepath= os.path.join(folderpath3,RSFilename)
            
            savefile=codecs.open(RESULTfilepath,"w","utf-8")
            
            fDEMPointer= open(DEMfilepath,"r")
            fFSPointer = open(FSfilepath,"r")
            while True:
                ResultLine=""
                DEMLine=(fDEMPointer.readline()).decode('utf-8').encode(type)
                FSLine=(fFSPointer.readline()).decode('utf-8').encode(type)
                if DEMLine:
                    DEMLine=DEMLine.strip()#删除文件中的指定字符
                    FSLine=FSLine.strip()
                    DEMValues=DEMLine.split(' ')#通过指定分隔符对字符串进行切片
                    FSValues=FSLine.split(' ')
                    for m in range(len(DEMValues)):
                        try:
                            DEMValue=float(DEMValues[m])
                            FSValue=float(FSValues[m])
                            tempPlus=DEMValue*DEMValue+FSValue*FSValue
                            sqrtRes=math.sqrt(tempPlus)
                            if m<len(DEMValues):
                                ResultLine=ResultLine+str(sqrtRes)+" "
                            else:
                                ResultLine=ResultLine+str(sqrtRes)
                        except:
                            pass

                    savefile.writelines(ResultLine)
                    savefile.writelines("\n")
                else:
                    break

            fDEMPointer.close()
            fFSPointer.close()
            savefile.close()
print "done"