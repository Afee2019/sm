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


def udbPrj(strUdb, strDt, strPrj):
	strAlias='t'
	if smu.OpenDataSource(strUdb, '', '', 'sceUDB', strAlias):
		smu.SetProjection(strAlias, strDt, strPrj)

def oraclePrj(server, user, pwd, strDt, strPrj):
	strAlias='t'
	if smu.OpenDataSource(server, user, pwd, 'sceOraclePlus', strAlias):
		smu.SetProjection(strAlias, strDt, strPrj)


'''
设置数据集投影
UDB数据源用法: SetProjection.py [bin] [c:/test.udb] [dtName] [c:/prj.xml]
Oracle数据源用法: SetProjection.py [bin] [server] [user] [pwd] [dtName] [c:/prj.xml]
'''

if __name__=='__main__':
	if len(sys.argv)>=5:
		bin = sys.argv[1]
		if os.path.exists(bin):
			sys.path.append(bin)
			import smu
		else:
			sys.exit()
		
		if len(sys.argv)==5:
			udb=sys.argv[2]
			dtname=sys.argv[3]
			prj=sys.argv[4]
			udbPrj(udb, dtname, prj)
		elif len(sys.argv)==7:
			server=sys.argv[2]
			user=sys.argv[3]
			pwd=sys.argv[4]
			dtname=sys.argv[5]
			prj=sys.argv[6]
			oraclePrj(server, user, ped, dtname, prj)
	
