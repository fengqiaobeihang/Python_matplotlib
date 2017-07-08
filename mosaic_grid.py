#coding=utf-8
import locale
import codecs
import sys
import re
import math
import arcpy
from   arcpy    import env
from   arcpy.sa import *
import os
import os.path
import sys

type=sys.getfilesystemencoding()

folderpath1="C:/Users/dy/Desktop/data/a/"
folderpath2="C:/Users/dy/Desktop/data/b/"
folderpath3="C:/Users/dy/Desktop/data/c/"
for dirpath,filename,filenames in os.walk(folderpath1):
	for filename in filenames:
		if os.path.splitext(filename)[1]=='.tif':
			gridafilepath=os.path.join(dirpath,filename)
			gridbFilename=filename.replace('a','b')
			RSFilename=filename.replace('a','c')
			gridbfilepath=os.path.join(folderpath2,gridbFilename)
			RESULTfilepath=os.path.join(folderpath3,RSFilename)

            inASCIIa = gridafilepath
            inASCIIb = gridbfilepath
            outname  = filename.replace('.tif','')
            print "ok"
            print gridafilepath
            print outname
            outRaster= RESULTfilepath+outname+".tif"
            arcpy.MosaicToNewRaster_management(inASCIIa,inASCIIb, outRaster,"8_BIT_UNSIGNED","40", "1", "LAST","FIRST")
            print "done"                     
                                   