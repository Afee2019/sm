# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as sm #����SuperMapģ��


#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	sm.Init()#��ʼ��Python�������;

	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtName = 'Dem2'
		sm.ExportRaster(odsAlias, dtName, 'fileSHP', r'F:\Temp\2012-08-25\test.shp')
		sm.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	sm.Exit()#�����������ͷ��ڴ�
