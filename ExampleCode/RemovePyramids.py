# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"D:\DotNetPythonBin\Bin") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ�������Oracle����ԴΪ��
server="sfc60" 
user="testMTT"
pwd="testMTT"
odsAlias="oracle"
dtName="RemovePyramids"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bRemove=SuperMap.RemovePyramids(odsAlias,dtName)#ɾ��Ӱ�������
    if bRemove == 1:
        print "ɾ���������ɹ�"
    else:
        print "ɾ��Ӱ�������ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"

SuperMap.Exit()#�����������ͷ��ڴ�
