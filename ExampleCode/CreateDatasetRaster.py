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
dtName="CreateDatasetRasterTest"
strType="Image" 
strEncType = "encDCT"
strPixfmt = "IPF_RGB"
iWidth=50
iHeight=50
dLeft = 0
dTop =50
dRight =50
dBottom =0
iBlkSize = 256
bMultiBands = 0
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#��oracle����Դ
if bOpen == 1:
    bCreate=SuperMap.CreateDatasetRaster(odsAlias,dtName,strType,strEncType,strPixfmt,
                                        iWidth,iHeight,dLeft,dTop,dRight,dBottom,iBlkSize)
    if bCreate == 1:
        print "����դ�����ݼ��ɹ�"
    else:
        print "����դ�����ݼ�ʧ��"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"
    
SuperMap.Exit()#�����������ͷ��ڴ�
