# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"D:\DotNetPythonBin\Bin") #��.net�����·�����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ�������Oracle����ԴΪ��
server="sfc60" 
user="testMTT"
pwd="testMTT"
odsAlias="oracle"
strDatasetSrc="DatasetSrcV"
strNewDtName="DatasetNew"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bCreate=SuperMap.CreateDatasetFrom(odsAlias,strDatasetSrc,odsAlias,strNewDtName,'encNONE')#ģ�崴�����ݼ�
    if bCreate == 1:
        print "ģ���½����ݼ��ɹ�"
    else:
        print "ģ���½����ݼ�ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"
    
SuperMap.Exit()#�����������ͷ��ڴ�