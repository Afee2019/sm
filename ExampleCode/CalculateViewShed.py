# coding: GB2312

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
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#������Դ
	if bOpen == 1:
		dtGrid = 'Dem2'
		x1=726628.410093674
		y1=3140482.5278305
		z1=2953
		sm.DeleteDataset(odsAlias, 'dem22')
		sm.CalculateViewShed(odsAlias, dtGrid, x1,y1,z1,0,360,-1, odsAlias, 'dem22')
		sm.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	sm.Exit()#�����������ͷ��ڴ�
