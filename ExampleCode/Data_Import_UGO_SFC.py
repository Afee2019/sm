# coding: GB2312
#ͨ�����д���ִ���谴˳������:
#1.�ű���2.UGO Bin��3.����·����4.����Դ·����server����5.����ԴUser
#6.����ԴPwd��7.�������ͣ�sceSDBPlus/sceOraclePlus��
#8.������������(���ִ�Сд,��GDBRaster/GDBVector)

#֧�ֵ��������У�E00/SHP/COV/DWG/DXF/DGN/KML/KMZ/TAB/MIF/GML/MAPGIS/VEC/WMF/VCT
#              IMG/TIF/BMP/PNG/JPG/GIF/GRD/RAW/DEM/SID/ECW/IDR/FST/BIP/BIL/BSQ

#===================����ģ��=============================
import sys
import string
import re
import os
import time

#=======================================================
#����ȫ�ֲ���
odsAlias="importtest"
importMode="GIS"
#=======================================================

#�����־
def WriteLog(tmpstr):
    logfilename = os.path.dirname(ugoPath)+"/Import.log"  #��־���·��
    time_str = time.strftime("%Y-%m-%d %H:%M:%S	",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logfilename,"a")
    f.write(logstr)
    f.close()


#���������·�����ļ���ֱ�Ӹ�ֵ��datafiles�����ļ���������ļ���
#ƥ��������ʽ������������append��datafiles������׷��
def visi(DataPath,ftype):    
    reMatch = "[\d\D]*." + fType
    datafiles = []
    if DataPath[-4:]=="." + fType or ftype.lower()=="cov":
        datafiles=[DataPath]       
    else:
        #ƥ��������ʽ������������append��datafiles������׷��DataPath�������ļ�
        for root, dirs, files in os.walk(DataPath):
            for file in files:
                if (re.match(reMatch,file)):
                    datafiles.append(os.path.join(root, file))
    return datafiles


#ͨ��SFC����
def SFCImport(file,targetName,startTime):
    if engtype=="sceSDBPlus":
        bOpen = SuperMap.OpenDataSource(server,"",engtype,odsAlias)
    elif engtype=="sceOraclePlus":
        bOpen = SuperMap.OpenDataSource("SERVER = "+server+";Database = "+user+";", "UID = "+user+";PWD ="+pwd,engtype,odsAlias)
    else:
        print "�������Ͳ�֧��"
        bOpen=0
    if bOpen == 1:
        bImport = SuperMap.ImportData(odsAlias,"",file,"",targetName+"P",targetName+"L",targetName+"R",targetName+"T",targetName+"N",targetName,fileType,"encNONE",0,0);
        if bImport == 1:
            endTime=time.time()
            WriteLog("\n����"+file+"��������ʱ"+str(endTime-startTime)+"   ")
        else:
            WriteLog("\n����"+file+"ʧ��")
        SuperMap.CloseDataSource(odsAlias)
    else:
        print "������Դʧ�ܣ�"


#ͨ��UGO����

def UGOImport(datafiles):        
        for file in datafiles: 
            WriteLog("\n����"+file+"��ʼ")
            targetNameTemp = file.split("\\")
            targetName=targetNameTemp[len(targetNameTemp)-1].split(".")[0]
            startTime=time.time()
            if IsSfcType(fType):
                SuperMapUGO.Exit()
                SFCImport(file,targetName,startTime)
            else:
                if IsRaster(fType):                
                    bimport=SuperMapUGO.ImportRasterFile(odsAlias,targetName,"encNONE",fileType,file)
                else:                
                    bimport=SuperMapUGO.ImportVectorFile(odsAlias, targetName, "encNONE", fileType, file,importMode)            
                if bimport==1:                
                    endTime=time.time() 
                    WriteLog("\n����"+file+"��������ʱ"+str(endTime-startTime)+"   ")
                else:
                    SuperMapUGO.Exit()                
                    SFCImport(file,targetName,startTime)
        SuperMapUGO.CloseDataSource(odsAlias)
            
                
#�ж����ݸ�ʽ�Ƿ�Ϊդ��դ�񷵻�True
def IsRaster(importFileType):
    DataType=importFileType.lower()
    fileTypes=["img","tif","bmp","png","jpg","gif","grd","raw","bip", \
               "bil","bsq","sid","ecw","idr","fst"]
    for afileType in fileTypes:
        if DataType==afileType:
            return 1
        else:
            return 0

#�ж��Ƿ���SFC֧�ֵĸ�ʽ
def IsSfcType(fType):
    sfTypes=fType.lower()
    if sfTypes==["e00","cov","dgn","gml","wal","wat","wap","wan","vec","wmf", \
             "vct","dem","bip","bil","bsq","sid","ecw","idr","fst","gdb"]:
        return 1
    else:
        return 0
    
#================================main����========================================
if __name__ =='__main__':    
    if len(sys.argv)==8:
        #============�������================
        ugoPath=sys.argv[1]
        DataPath=sys.argv[2]
        server=sys.argv[3]
        user=sys.argv[4]
        pwd=sys.argv[5]
        engtype=sys.argv[6]
        fType=sys.argv[7] 
        #====================================
        sfcPath=ugoPath+"\sfc"
        sys.path.append(sfcPath)
        os.sys.path.append(ugoPath)        
        import smu as SuperMapUGO
        import SuperMap
        SuperMapUGO.Init()
        SuperMap.Init()        
        if SuperMapUGO.OpenDataSource(server, user, pwd, engtype, odsAlias):
            print "����Դ�򿪳ɹ�"
            if fType.lower()=="wal" or fType.lower()=="wan" or fType.lower()=="wat" \
               or fType.lower()=="wap":
                fileType="fileMAPGIS"            
            else:
                fileType="file"+fType.upper()         
            #�����ļ��к󣬵��õ��뺯��
            bvisi=visi(DataPath,fType)
            UGOImport(bvisi)
        else:
            print "����Դ��ʧ��"
        SuperMapUGO.Exit()#��ջ������ͷ��ڴ�
        SuperMap.Exit()#��ջ���
       
    else:
        print "�����������!"
        print "============�밴˳������:================"
        print "1.�ű�\n2.UGO Bin\n3.����·��\n4.����Դ·��(server)\n5.����Դ(User)"
        print "6.����Դ(Pwd)\n7.�������ͣ�sceSDBPlus/sceOraclePlus)\n8.������������(���ִ�Сд)"
        print "=========================================="
