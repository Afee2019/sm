# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"G:\01_SourceCode_7.0.0_B\Builds\Win_Solution_vc11\BinD_Unicode") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"E:\2012-02-20\2013-07-29\eeeeeee.udb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceUDB",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtGrid1 = 'srtm_01_02_1'
		dtGrid2 = 'DemData'
		#SuperMap.DeleteDataset(odsAlias, dtGrid2)
		L = SuperMap.ExtractIsoline(odsAlias, dtGrid1, 0,100,3,0,0,odsAlias, dtGrid2,"asdfa")
		print L
		SuperMap.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	SuperMap.Exit()#�����������ͷ��ڴ�
