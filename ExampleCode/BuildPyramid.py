# coding: GB2312

#===================================
import os
import sys
import time
#====================================


def printTime():
	now = time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time()))
	print now

def main(server, user, pwd, engtype, dtName):
	odsAlias="oracle"
	bOpen=smu.OpenDataSource(server,user, pwd, engtype,odsAlias)
	if bOpen == 1:
		if dtName=="''":
			dtName=smu.GetDatasetName(odsAlias, 0)
		bBuild=smu.BuildPyramid(odsAlias,dtName)#创建影像金字塔
		if bBuild == 1:
			print "创建金字塔成功"
		else:
			print "创建影像金字塔失败！"
		smu.CloseDataSource(odsAlias)
	else:
		print "打开数据源失败！"
	
	smu.Exit()#清空组件环境释放内存

def udb(server, dtName):
	main(server, '', '', 'sceUDB', dtName)

def oracle(server, user, pwd, dtName):
	main(server, user, pwd, 'sceOraclePlus', dtName)

'''
创建金字塔
udb数据源: BuildPyramid.py [Bin] [udb] [dtName]
oracle数据源: BuildPyramid.py [Bin] [server] [user] [pwd] [dtName]
dtName为空时,将对第一个数据集创建金字塔
'''

if __name__=='__main__':
	if len(sys.argv) >= 4:
		ugo = sys.argv[1]
		if os.path.exists(ugo):
			sys.path.append(ugo) #将.net组件的路径添加到环境变量
			import smu
		else:
			sys.exit()
	else:
		sys.exit()

	print len(sys.argv), sys.argv
	printTime()
	if len(sys.argv)==4:
		server=sys.argv[2]
		dtname=sys.argv[3]
		udb(server, dtname)
	elif len(sys.argv)==6:
		server=sys.argv[2]
		user=sys.argv[3]
		pwd=sys.argv[4]
		dtname=sys.argv[5]
		oracle(server, user, pwd, dtname)		
	printTime()

