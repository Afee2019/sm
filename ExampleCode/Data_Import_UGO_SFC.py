# coding: GB2312
#通过运行窗口执行需按顺序输入:
#1.脚本、2.UGO Bin、3.数据路径、4.数据源路径（server）、5.数据源User
#6.数据源Pwd、7.引擎类型（sceSDBPlus/sceOraclePlus）
#8.导入数据类型(区分大小写,如GDBRaster/GDBVector)

#支持导入类型有：E00/SHP/COV/DWG/DXF/DGN/KML/KMZ/TAB/MIF/GML/MAPGIS/VEC/WMF/VCT
#              IMG/TIF/BMP/PNG/JPG/GIF/GRD/RAW/DEM/SID/ECW/IDR/FST/BIP/BIL/BSQ

#===================加载模块=============================
import sys
import string
import re
import os
import time

#=======================================================
#几个全局参数
odsAlias="importtest"
importMode="GIS"
#=======================================================

#输出日志
def WriteLog(tmpstr):
    logfilename = os.path.dirname(ugoPath)+"/Import.log"  #日志输出路径
    time_str = time.strftime("%Y-%m-%d %H:%M:%S	",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logfilename,"a")
    f.write(logstr)
    f.close()


#传入的数据路径是文件则直接赋值给datafiles；是文件夹则遍历文件夹
#匹配正则表达式，符合条件的append到datafiles，用于追加
def visi(DataPath,ftype):    
    reMatch = "[\d\D]*." + fType
    datafiles = []
    if DataPath[-4:]=="." + fType or ftype.lower()=="cov":
        datafiles=[DataPath]       
    else:
        #匹配正则表达式，符合条件的append到datafiles，用于追加DataPath中所有文件
        for root, dirs, files in os.walk(DataPath):
            for file in files:
                if (re.match(reMatch,file)):
                    datafiles.append(os.path.join(root, file))
    return datafiles


#通过SFC导入
def SFCImport(file,targetName,startTime):
    if engtype=="sceSDBPlus":
        bOpen = SuperMap.OpenDataSource(server,"",engtype,odsAlias)
    elif engtype=="sceOraclePlus":
        bOpen = SuperMap.OpenDataSource("SERVER = "+server+";Database = "+user+";", "UID = "+user+";PWD ="+pwd,engtype,odsAlias)
    else:
        print "引擎类型不支持"
        bOpen=0
    if bOpen == 1:
        bImport = SuperMap.ImportData(odsAlias,"",file,"",targetName+"P",targetName+"L",targetName+"R",targetName+"T",targetName+"N",targetName,fileType,"encNONE",0,0);
        if bImport == 1:
            endTime=time.time()
            WriteLog("\n导入"+file+"结束，耗时"+str(endTime-startTime)+"   ")
        else:
            WriteLog("\n导入"+file+"失败")
        SuperMap.CloseDataSource(odsAlias)
    else:
        print "打开数据源失败！"


#通过UGO导入

def UGOImport(datafiles):        
        for file in datafiles: 
            WriteLog("\n导入"+file+"开始")
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
                    WriteLog("\n导入"+file+"结束，耗时"+str(endTime-startTime)+"   ")
                else:
                    SuperMapUGO.Exit()                
                    SFCImport(file,targetName,startTime)
        SuperMapUGO.CloseDataSource(odsAlias)
            
                
#判断数据格式是否为栅格，栅格返回True
def IsRaster(importFileType):
    DataType=importFileType.lower()
    fileTypes=["img","tif","bmp","png","jpg","gif","grd","raw","bip", \
               "bil","bsq","sid","ecw","idr","fst"]
    for afileType in fileTypes:
        if DataType==afileType:
            return 1
        else:
            return 0

#判断是否是SFC支持的格式
def IsSfcType(fType):
    sfTypes=fType.lower()
    if sfTypes==["e00","cov","dgn","gml","wal","wat","wap","wan","vec","wmf", \
             "vct","dem","bip","bil","bsq","sid","ecw","idr","fst","gdb"]:
        return 1
    else:
        return 0
    
#================================main函数========================================
if __name__ =='__main__':    
    if len(sys.argv)==8:
        #============输入参数================
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
            print "数据源打开成功"
            if fType.lower()=="wal" or fType.lower()=="wan" or fType.lower()=="wat" \
               or fType.lower()=="wap":
                fileType="fileMAPGIS"            
            else:
                fileType="file"+fType.upper()         
            #遍历文件夹后，调用导入函数
            bvisi=visi(DataPath,fType)
            UGOImport(bvisi)
        else:
            print "数据源打开失败"
        SuperMapUGO.Exit()#清空环境，释放内存
        SuperMap.Exit()#清空环境
       
    else:
        print "输入参数错误!"
        print "============请按顺序输入:================"
        print "1.脚本\n2.UGO Bin\n3.数据路径\n4.数据源路径(server)\n5.数据源(User)"
        print "6.数据源(Pwd)\n7.引擎类型（sceSDBPlus/sceOraclePlus)\n8.导入数据类型(区分大小写)"
        print "=========================================="
