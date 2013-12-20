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
		bBuild=smu.BuildPyramid(odsAlias,dtName)#����Ӱ�������
		if bBuild == 1:
			print "�����������ɹ�"
		else:
			print "����Ӱ�������ʧ�ܣ�"
		smu.CloseDataSource(odsAlias)
	else:
		print "������Դʧ�ܣ�"
	
	smu.Exit()#�����������ͷ��ڴ�

def udb(server, dtName):
	main(server, '', '', 'sceUDB', dtName)

def oracle(server, user, pwd, dtName):
	main(server, user, pwd, 'sceOraclePlus', dtName)

'''
����������
udb����Դ: BuildPyramid.py [Bin] [udb] [dtName]
oracle����Դ: BuildPyramid.py [Bin] [server] [user] [pwd] [dtName]
dtNameΪ��ʱ,���Ե�һ�����ݼ�����������
'''

if __name__=='__main__':
	if len(sys.argv) >= 4:
		ugo = sys.argv[1]
		if os.path.exists(ugo):
			sys.path.append(ugo) #��.net�����·����ӵ���������
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

