# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as sm #����SuperMapģ��

sm.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		sm.ExportRaster(odsAlias, dtGrid1, 'fileTIF', r'F:\Temp\2012-08-25\test.tif')
		sm.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	sm.Exit()#�����������ͷ��ڴ�
