# coding: GB2312

import sys
import string
import re
import os
import time


#=====================================
#��Ҫ�޸ĵĲ���  
odsAlias="odsAlias"
testPath="F:\\2012\\python��������\\Data\\ImportVectorFile\\Countries.shp"
fileType ="fileSHP"
#��Ҫ�޸ĵĲ���
#=====================================

def to_udb(udb, fileType, filePath):
	isOpen=smu.OpenDataSource(udb, '', '', 'sceUDB', odsAlias)
	smu.DeleteDataset(odsAlias, dtName)
	#����ʸ���ļ�
	bImport = smu.ImportVectorFile(odsAlias,'test', "encBYTE",fileType, filePath, "GIS")
	pass

def to_db(server, user, pwd, fileType, filePath):
	#������Դ
	bOpen = smu.OpenDataSource(server,user,pwd,"sceOraclePlus",odsAlias)
	if bOpen == 1:
		#����ʸ���ļ�
		bImport = smu.ImportVectorFile(odsAlias,'test', "encBYTE",fileType, filePath, "GIS")
		if bImport == 1:
			print "����ɹ�"
		else:
			print "����ʧ�ܣ�"
			smu.CloseDataSource(odsAlias)
	else:
		print "������Դʧ�ܣ�"
		smu.Exit()#��ջ������ͷ��ڴ�

if __name__=='__main__':
	if len(sys.argv)==2:
		ugopath=sys.argv[1]
		sys.path.append(ugopath)
		import smu 
		smu.Init()
		pass
