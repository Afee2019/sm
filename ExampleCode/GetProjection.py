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


def main(strType, strFile, strPrj):
	strType = getType(strType)
	if smu.GetProjection(strType, strFile, strPrj):
		print strPrj
	else:
		print 'Can not get projection.'



'''
获取文件投影信息,保存到指定的文件中
用法: GetProjection.py [bin] [tif] [file] [prjfile]
'''

if __name__=='__main__':
	if len(sys.argv)==5:
		bin = sys.argv[1]
		if os.path.exists(bin):
			sys.path.append(bin)
			import smu
		else:
			sys.exit()

		type = sys.argv[2]
		file = sys.argv[3]
		prj = sys.argv[4]
		main(type, file, prj)
