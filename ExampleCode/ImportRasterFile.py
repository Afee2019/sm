# coding: GB2312

import sys
import string
import re
import os
import time

def getType(ext):
	if ext.lower() == 'tif':
		fileType='fileTIF'
	elif ext.lower() == 'img':
		fileType='fileIMG'

	return fileType

def printTime():
	now = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))
	print now

def toUDB(file):
	iPos = file.find('.')
	ext = file[iPos+1:len(file)]
	fileType = 'fileTIF'
	fileType = getType(ext) 
	
	udb = file[0:iPos+1]+'udb'
	udd = file[0:iPos+1]+'udd'
	if os.path.exists(udb):
		os.remove(udb)
	if os.path.exists(udd):
		os.remove(udd)
	
	odsAlias='test'
	if smu.CreateDataSource(udb, '', '', 'sceUDB', odsAlias):
		if smu.ImportRasterFile(odsAlias, 't', 'encDCT', fileType, file):
			print '导入成功:', udb
		else:
			print '导入失败:', file



def toDB(server, user, pwd, file):
	iPos = file.find('.')
	ext = file[iPos+1:len(file)]
	fileType = getType(ext)

	odsAlias = 'test'
	if smu.OpenDataSource(server, user, pwd, 'sceOraclePlus', odsAlias):
		dtName='t'
		smu.DeleteDataset(odsAlias, dtName)
		if smu.ImportRasterFile(odsAlias, dtName, 'encDCT', fileType, file):
			print '导入成功:', file
		else:
			print '导入失败:', file

'''
将文件导入到udb/oracle数据源中
导入到UDB用法: ImportRasterFile.py [bin] [c:/test.tif]
导入到Oracle用法: ImportRasterFile.py [bin] [server] [user] [pwd] [c:/test.tif]
'''

if __name__=='__main__':
	if len(sys.argv)>=3:
		bin = sys.argv[1]
		if os.path.exists(bin):
			sys.path.append(bin)
			import smu
		else:
			sys.exit()
		
		if len(sys.argv)==3:
			file=sys.argv[2]
			printTime()
			toUDB(file)
			printTime()
			smu.Exit()
		elif len(sys.argv)==6:
			server=sys.argv[2]
			user=sys.argv[3]
			pwd=sys.argv[4]
			file=sys.argv[5]
			printTime()
			toDB(server, user, pwd, file)
			printTime()
			smu.Exit()
	
