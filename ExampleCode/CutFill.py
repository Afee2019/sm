# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\�������.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		dtGrid2 = 'DemData'
		SuperMap.DeleteDataset(odsAlias, 'dem22')
		L = SuperMap.CutFill(odsAlias, dtGrid1, dtGrid2,odsAlias, 'dem22')
		print L
		SuperMap.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	SuperMap.Exit()#�����������ͷ��ڴ�
