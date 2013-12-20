# coding: GB2312

import sys
import string
import re
import os
import time


#=====================================
#需要修改的参数  
odsAlias="odsAlias"
testPath="F:\\2012\\python范例程序\\Data\\ImportVectorFile\\Countries.shp"
fileType ="fileSHP"
#需要修改的参数
#=====================================

def to_udb(udb, fileType, filePath):
	isOpen=smu.OpenDataSource(udb, '', '', 'sceUDB', odsAlias)
	smu.DeleteDataset(odsAlias, dtName)
	#导入矢量文件
	bImport = smu.ImportVectorFile(odsAlias,'test', "encBYTE",fileType, filePath, "GIS")
	pass

def to_db(server, user, pwd, fileType, filePath):
	#打开数据源
	bOpen = smu.OpenDataSource(server,user,pwd,"sceOraclePlus",odsAlias)
	if bOpen == 1:
		#导入矢量文件
		bImport = smu.ImportVectorFile(odsAlias,'test', "encBYTE",fileType, filePath, "GIS")
		if bImport == 1:
			print "导入成功"
		else:
			print "导入失败！"
			smu.CloseDataSource(odsAlias)
	else:
		print "打开数据源失败！"
		smu.Exit()#清空环境，释放内存

if __name__=='__main__':
	if len(sys.argv)==2:
		ugopath=sys.argv[1]
		sys.path.append(ugopath)
		import smu 
		smu.Init()
		pass
