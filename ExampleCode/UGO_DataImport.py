# coding: GB2312
#ͨ�����д���ִ���谴˳������:
#1.�ű���2.UGO Bin��3.����·����4.����Դ·����server����5.����ԴUser
#6.����ԴPwd��7.�������ͣ�sceSDBPlus/sceUDB/sceOraclePlus��
#8.������������(���ִ�Сд,��GDBRaster/GDBVector)

#֧�ֵ��������У�E00/SHP/GDBVector/AIBinCov/DWG/DXF/DGN/KML/KMZ/TAB/MIF
#              IMG/TIF/BMP/PNG/JPG/GIF/GRD/RAW

#=========����ģ��=================================
import sys
import string
import re
import os
import time
#==================================================

#==================================================
#����ȫ�ֲ���
odsAlias="conversion"
importMode="GIS"
datafiles = []
#==================================================

#�����־
def WriteLog(tmpstr):
    logfilename = os.path.dirname(ugoPath)+"/Import.log"  #��־���·��
    time_str = time.strftime("%Y-%m-%d %H:%M:%S	",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logfilename,"a")
    f.write(logstr)
    f.close()

def Visit(DataPath):
    reMatch = "[\d\D]*."+fType 

    #ƥ��������ʽ������������append��datafiles������׷��DataPath�������ļ�   
    for root, dirs, files in os.walk(DataPath):
        for file in files:
            if (re.match(reMatch,file)):
                datafiles.append(os.path.join(root, file))
    return datafiles

#ͨ��UGO����ʸ���ļ�
def UGOImportVector(DataPath,IsUserFME,dataArray):    
    if bopen==1:
        print "������Դ�ɹ�"
        for file in dataArray:
            print str(file)
            #�ж�����Ҫ�ĸ�ʽ�Ž��е���                
            WriteLog("\n����"+file+"��ʼ")
            #����ʸ���ļ�                    
            targetNameTemp = file.split("\\")
            targetName=targetNameTemp[len(targetNameTemp)-1].split(".")[0]
            SuperMap.SetUseFME(IsUserFME)                
            startTime=time.time()
            bimport=SuperMap.ImportVectorFile(odsAlias, targetName, "encNONE", fileType, file,importMode)                
            if bimport==1:                        
                    endTime=time.time()
                    cost=endTime-startTime                        
                    WriteLog("\n����"+file+"��������ʱ"+str(cost)+"   ")                       
            else:           
                    SuperMap.SetUseFME(True)
                    bimport=SuperMap.ImportVectorFile(odsAlias, targetName, "encNONE", fileType, file,importMode)
              
        SuperMap.CloseDataSource(odsAlias)

        
#ͨ��UGO����դ���ļ�
def UGOImportRaster(DataPath,IsUserFME,dataArray):
    for file in dataArray:                               
        WriteLog("\n����"+file+"��ʼ")
        #����ʸ���ļ�                    
        targetNameTemp = file.split("\\")
        targetName=targetNameTemp[len(targetNameTemp)-1].split(".")[0]
        SuperMap.SetUseFME(IsUserFME)                
        startTime=time.time()
        bimport=SuperMap.ImportRasterFile(odsAlias,targetName,"encNONE",fileType,file)                
        if bimport==1:                        
                endTime=time.time()
                cost=endTime-startTime                        
                WriteLog("\n����"+file+"��������ʱ"+str(cost)+"   ")                       
        else:           
                SuperMap.SetUseFME(True)
                bimport=SuperMap.ImportRasterFile(odsAlias,targetName,"encNONE",fileType,file)               
    SuperMap.CloseDataSource(odsAlias)                


#�жϸ�ʽ��UGO֧�ָ�ʽ����0��FME֧�ָ�ʽ����1
def IsUseFME(importFileType):
    DataType=importFileType.lower()
    if DataType=="e00" or  DataType=="gdb" or DataType=="gml" \
       or DataType=="dgn" or DataType=="aibincov":
        return 1
    else:
        return 0
#�ж����ݸ�ʽ�Ƿ�Ϊդ��դ�񷵻�True
def IsRaster(importFileType):
    DataType=importFileType.lower()
    if DataType=="img" or DataType=="tif" or DataType=="bmp" or DataType=="png" \
       or DataType=="jpg" or DataType=="gif" or DataType=="grd"  or DataType=="raw":
       return 1
    else:
        return 0

#==========================main����=============================================   
if __name__ =='__main__':
    #SuperMap.Init()
    if len(sys.argv)==8:
        #============�������================
        ugoPath=sys.argv[1]
        DataPath=sys.argv[2]
        server=sys.argv[3]
        user=sys.argv[4]
        pwd=sys.argv[5]
        engtype=sys.argv[6]
        fType=sys.argv[7]        
        fileType="file"+fType.upper()
        #====================================
        os.sys.path.append(ugoPath)        
        import smu as SuperMap        
        SuperMap.Init()        
        bUserFME=IsUseFME(fType)
        bopen=SuperMap.OpenDataSource(server, user, pwd, engtype, odsAlias)
        if bopen==1:
            print "������Դ�ɹ�"
            #�ж����������Ƿ����ļ������ݣ��ļ��͵Ĵ��ļ��У�����gdb��
            if fType=="AIBinCov" or fType=="GDBVector" :
                SuperMap.SetUseFME(True)
                if fType=="GDBRaster":                     
                    b=SuperMap.ImportRasterFile(odsAlias, "", "encNONE", fileType, DataPath,importMode)
                else:
                    b=SuperMap.ImportVectorFile(odsAlias, "", "encNONE", fileType, DataPath,importMode)
                if b:
                    print fType+"����ɹ�"
                else:
                    print fType+"����ʧ��"
                    
            else: 
                bVisi=Visit(DataPath)
                if IsRaster:                
                    UGOImportRaster(DataPath,bUserFME,bVisi)
                else:                
                    UGOImportVector(DataPath,bUserFME,bVisi)
        else:
            print "������Դʧ��"
        SuperMap.Exit()#��ջ������ͷ��ڴ�
    else:        
        print "�����������!"
        print "============�밴˳������:================"
        print "1.�ű�\n2.UGO Bin\n3.����·��\n4.����Դ·��(server)\n5.����Դ(User)"
        print "6.����Դ(Pwd)\n7.�������ͣ�sceSDBPlus/sceUDB/sceOraclePlus)\n8.������������(���ִ�Сд)"
        print "=========================================="
