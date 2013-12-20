# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:48:13 2012

@author: supermap
"""
import sys
import string
import re
import os
import time

import SMUP

#根据文件扩展名返回规范的文件类型描述符.
def getType(ext):
	if ext.lower() == 'tif':
		return 'fileTIF'
	elif ext.lower() == 'img':
		return 'fileIMG'

#扫描指定目录下的制定扩展名文件,返回全路径文件名列表.  
def scanPath(type, path):
	datafiles = []
	reMatch = '[\d\D]*.tif$'
	if type=='img':
		reMath = '[\d\D]*.img$'	
	for root, dirs, files in os.walk(path):
		for file in files:
			if (re.match(reMatch,file)):
				datafiles.append(os.path.join(root, file))
	return datafiles

#根据行列数构建datafiles，用于追加    
def BuildFileListCol(type, path, nCol):
	print ""
	print("----------Build Files List-----------")	
	
	R01=3
	R02=4
	
	#nCol = int(Col)
	print("Col: %(C00)02d" % {"C00": nCol})
	print("Row: %(R01)02d-%(R02)02d" % {"R01":R01,"R02":R02})

	strFileName =""
	strFilePath =""
	FileCount = 0
	for j in range(R01,R02):
		#ConvertTif2UDBOnce(path,nCol,j)
		FileCount = FileCount + 1
		print("Files Count: %(FC)02d" % {"FC":FileCount})
	return FileCount
 
#根据行列数构建datafiles，用于追加
def buildFileList(type, path):
	print ""
	print("----------Build Files List-----------")	
	datafiles = []
	
	C01=46
	C02=48
	R01=1
	R02=5	
	print("Col: %(C01)02d-%(C02)02d" % {"C01":C01,"C02":C02})
	print("Row: %(R01)02d-%(R02)02d" % {"R01":R01,"R02":R02})

	strFileName =""
	strFilePath =""
	FileCount = 0
	for i in range(C01,C02):
		for j in range(R01,R02):
			#ConvertTif2UDBOnce(path,i,j)
			FileCount = FileCount + 1
			print("Files Count: %(FC)02d" % {"FC":len(FileCount)})
	return datafiles
 
#将列表中的信息保存到指定的文件中. 
def list2File(filepath,xlist):
     print "Save list to file"
     f = open(filepath, "a")
     for line in xlist:
          f.write(line+'\r\n')
     f.close()

#根据全路径得到文件名,不含扩展名.
def getFileName(file):
    filepath = os.path.split(file)
    print 'filepath: ',filepath
    lists = filepath[1].split('.')
    filename = lists[0]
    print 'filename: ',filename
    return filename
    
#获取指定影像文件的像素格式.
def getPixelFormatOne(fileType, file):
	print "SMUP:GetPixelFormat @ ",file
	pixType = SMUP.smu.GetImagePixelFormatName(fileType, file)
	return pixType

#获取像素格式,找到第一个实际存在的文件,返回该文件像素格式.
def getPixelFormat(fileType, files):
	print("SMUP:GetPixelFormat @ ALL Files.---")	
	for file in files:
		if os.path.exists(file):
			pixType = SMUP.smu.GetImagePixelFormatName(fileType, file)
			return pixType
 
#计算指定文件的范围等信息,返回一特殊数据结构. 
def calcDatasetInfoOne(type,file):
	print("----------CalcDataFileInfo-----------")	
	L=[]	
	left=[]
	top=[]
	right=[]
	bottom=[]
	ratiox=[]
	ratioy=[]

	#获取每个影像文件的左右地理范围，保存到数组
	if os.path.exists(file):
		L= SMUP.smu.GetImageGeoRef(type,file)
		print file
		print "File Extend: ", L

		l=float(L[0][0])
		t=float(L[0][1])
		r=float(L[0][2])
		b=float(L[0][3])
		w=int(L[1][0])
		h=int(L[1][1])
		x=(r-l)/w
		y=(t-b)/h
		
		left.append(l)
		right.append(r)
		top.append(t)
		bottom.append(b)
		ratiox.append(x)
		ratioy.append(y)

		#获取左右上下边界
		dLeft=min(left)
		dRight=max(right)
		dTop=max(top)
		dBottom=min(bottom)
			
		#获取分辨率，影像最小分辨率作为数据集分辨率
		dRatioX = min(ratiox)
		dRatioY = min(ratioy)
		
		#计算影像数据集宽度和高度
		nWidth = int((dRight-dLeft)/dRatioX)
		nHeight = int((dTop-dBottom)/dRatioY)
		
		#重新计算，保证分辨率正确
		dRight=dLeft+dRatioX*nWidth
		dBottom=dTop-dRatioY*nHeight
		L = [nWidth, nHeight, dLeft, dTop, dRight, dBottom]	
	else:
		print("File NoExist:" + file)
		#L = [100, 100, 0, 0, 100, 100]			
	return L
 
#计算列表中所有文件的范围等信息,返回一特殊数据结构.     
def calcDatasetInfo(type, datafiles):
	print("----------Calc DataFiles Info-----------")	
	L=[]	
	left=[]
	top=[]
	right=[]
	bottom=[]
	ratiox=[]
	ratioy=[]

	#获取每个影像文件的左右地理范围，保存到数组
	for file in datafiles:
		if os.path.exists(file):
			L= SMUP.smu.GetImageGeoRef(type,file)
			#print file
			#print "File Extend: ", L

			l=float(L[0][0])
			t=float(L[0][1])
			r=float(L[0][2])
			b=float(L[0][3])
			w=int(L[1][0])
			h=int(L[1][1])
			x=(r-l)/w
			y=(t-b)/h
		
			left.append(l)
			right.append(r)
			top.append(t)
			bottom.append(b)
			ratiox.append(x)
			ratioy.append(y)

			#获取左右上下边界
			dLeft=min(left)
			dRight=max(right)
			dTop=max(top)
			dBottom=min(bottom)
			
			#获取分辨率，影像最小分辨率作为数据集分辨率
			dRatioX = min(ratiox)
			dRatioY = min(ratioy)
		
			#计算影像数据集宽度和高度
			nWidth = int((dRight-dLeft)/dRatioX)
			nHeight = int((dTop-dBottom)/dRatioY)
		
			#重新计算，保证分辨率正确
			dRight=dLeft+dRatioX*nWidth
			dBottom=dTop-dRatioY*nHeight
			L = [nWidth, nHeight, dLeft, dTop, dRight, dBottom]	
		else:
			print("File NoExist:" + file)
			#L = [100, 100, 0, 0, 100, 100]			
	return L

#删除已存在的输出文件
def clearFile(dtFile):
	#清理初始环境,需要调整...
	udb = dtFile + '.udb'
	udd = dtFile + '.udd'
	if os.path.exists(udb):
		os.remove(udb)
	if os.path.exists(udd):
		os.remove(udd)
  
#将所有TIF文件转为分开的UDB,创建数据集。 
def Tif2UDB(flist,udbpath):
        for f in flist:
            Tif2UDBOne(f,udbpath)

#将指定TIF文件转为UDB,创建为一个数据集。 
def Tif2UDBOne(file,udbpath):
        print 'Tif2UDB: ',file,'\r\n'
        strFileName=getFileName(file)

        print 'Build FileName: ',strFileName,udbpath
        if os.path.exists(udbpath):
		print "Convert: " + udbpath
        else:
		print "Not Exist: " + udbpath
		exit()
	
        L=[]
        L=SMUP.smu.GetImageGeoRef(getType("TIF"),file)
        l=float(L[0][0])
        t=float(L[0][1])
        r=float(L[0][2])
        b=float(L[0][3])
        w=int(L[1][0])
        h=int(L[1][1])
    		
        pixType = getPixelFormatOne(getType("TIF"), file)
	
        odsAlias = strFileName
        dtName = odsAlias
        dtName = dtName.replace('-','_')
         
        dtFile = os.path.join(udbpath,dtName)	
        clearFile(dtFile)
        isOpen=SMUP.smu.OpenDataSource(udbpath+odsAlias,'','', 'sceUDB', odsAlias)
	
        #创建数据集		
        bCreate = SMUP.smu.CreateDatasetRaster(odsAlias,dtName, 
			'Image', 'encDCT', pixType, w, h , l, t, r , b, 256)
        SMUP.smu.AppendRasterFile(odsAlias,dtName,getType("tif"), file)

        #smu.BuildPyramid(odsAlias, dtName)
        SMUP.smu.CloseDataSource(odsAlias)
	
 #将TIF转为UDB	
def ConvertTif2UDBOnce(path,c,r):
	strFileName="N-%(C)02d-%(R)02d" % {"C":c,"R":r*5}
	strFilePath=os.path.join(path,"N-%(C)02d-%(R)02d.tif" % {"C":c,"R":r*5})	
	OutputPath = "H:\\ETM\\TIF_SM\\"
	
	dtFile = os.path.join(path,strFileName)
	
	print 'Build FileName: ',strFileName,dtFile	
	print "--Convert Block Files: ",strFilePath
	if os.path.exists(strFilePath):
		print "Convert: " + strFilePath
	else:
		print "Not Exist: " + strFilePath
		exit()
	
	L=[]
	L=SMUP.smu.GetImageGeoRef(getType("TIF"),strFilePath)
	print "File Extend: ", L

	l=float(L[0][0])
	t=float(L[0][1])
	r=float(L[0][2])
	b=float(L[0][3])
	w=int(L[1][0])
	h=int(L[1][1])
		
	pixType = getPixelFormat(getType("TIF"), strFilePath)
	print "Data Pixel Type: ",pixType	
	
	odsAlias = strFileName
	dtName = odsAlias
	dtName = dtName.replace('-','_')	
	print "Clear UDB File..."
	print dtName
	
	clearFile(dtFile)
	
	print "Create Datasource..."
	isOpen=SMUP.smu.OpenDataSource(OutputPath+odsAlias,'','', 'sceUDB', odsAlias)
	
	print "Import Dataset...",strFilePath
	#创建数据集		
	bCreate = SMUP.smu.CreateDatasetRaster(odsAlias,dtName, 
			'Image', 'encDCT', pixType, w, h , l, t, r , b, 256)
	SMUP.smu.AppendRasterFile(odsAlias,dtName,getType("tif"), strFilePath)
		
	print "BuildPyramid..."
	#SMUP.smu.BuildPyramid(odsAlias, dtName)
	SMUP.smu.CloseDataSource(odsAlias)
	print "==Finished.==========="