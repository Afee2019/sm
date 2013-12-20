# coding: GB2312
#通过运行窗口执行需按顺序输入:
#1.脚本、2.UGO Bin、3.数据路径、4.数据源路径（server）、5.数据源User
#6.数据源Pwd、7.引擎类型（sceSDBPlus/sceUDB/sceOraclePlus）
#8.导入数据类型(区分大小写,如GDBRaster/GDBVector)

#支持导入类型有：E00/SHP/GDBVector/AIBinCov/DWG/DXF/DGN/KML/KMZ/TAB/MIF
#              IMG/TIF/BMP/PNG/JPG/GIF/GRD/RAW

#=========加载模块=================================
import sys
import string
import re
import os
import time
#==================================================

#==================================================
#几个全局参数
odsAlias="conversion"
importMode="GIS"
datafiles = []
#==================================================

#输出日志
def WriteLog(tmpstr):
    logfilename = os.path.dirname(ugoPath)+"/Import.log"  #日志输出路径
    time_str = time.strftime("%Y-%m-%d %H:%M:%S	",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logfilename,"a")
    f.write(logstr)
    f.close()

def Visit(DataPath):
    reMatch = "[\d\D]*."+fType 

    #匹配正则表达式，符合条件的append到datafiles，用于追加DataPath中所有文件   
    for root, dirs, files in os.walk(DataPath):
        for file in files:
            if (re.match(reMatch,file)):
                datafiles.append(os.path.join(root, file))
    return datafiles

#通过UGO导入矢量文件
def UGOImportVector(DataPath,IsUserFME,dataArray):    
    if bopen==1:
        print "打开数据源成功"
        for file in dataArray:
            print str(file)
            #判断是需要的格式才进行导入                
            WriteLog("\n导入"+file+"开始")
            #导入矢量文件                    
            targetNameTemp = file.split("\\")
            targetName=targetNameTemp[len(targetNameTemp)-1].split(".")[0]
            SuperMap.SetUseFME(IsUserFME)                
            startTime=time.time()
            bimport=SuperMap.ImportVectorFile(odsAlias, targetName, "encNONE", fileType, file,importMode)                
            if bimport==1:                        
                    endTime=time.time()
                    cost=endTime-startTime                        
                    WriteLog("\n导入"+file+"结束，耗时"+str(cost)+"   ")                       
            else:           
                    SuperMap.SetUseFME(True)
                    bimport=SuperMap.ImportVectorFile(odsAlias, targetName, "encNONE", fileType, file,importMode)
              
        SuperMap.CloseDataSource(odsAlias)

        
#通过UGO导入栅格文件
def UGOImportRaster(DataPath,IsUserFME,dataArray):
    for file in dataArray:                               
        WriteLog("\n导入"+file+"开始")
        #导入矢量文件                    
        targetNameTemp = file.split("\\")
        targetName=targetNameTemp[len(targetNameTemp)-1].split(".")[0]
        SuperMap.SetUseFME(IsUserFME)                
        startTime=time.time()
        bimport=SuperMap.ImportRasterFile(odsAlias,targetName,"encNONE",fileType,file)                
        if bimport==1:                        
                endTime=time.time()
                cost=endTime-startTime                        
                WriteLog("\n导入"+file+"结束，耗时"+str(cost)+"   ")                       
        else:           
                SuperMap.SetUseFME(True)
                bimport=SuperMap.ImportRasterFile(odsAlias,targetName,"encNONE",fileType,file)               
    SuperMap.CloseDataSource(odsAlias)                


#判断格式，UGO支持格式返回0，FME支持格式返回1
def IsUseFME(importFileType):
    DataType=importFileType.lower()
    if DataType=="e00" or  DataType=="gdb" or DataType=="gml" \
       or DataType=="dgn" or DataType=="aibincov":
        return 1
    else:
        return 0
#判断数据格式是否为栅格，栅格返回True
def IsRaster(importFileType):
    DataType=importFileType.lower()
    if DataType=="img" or DataType=="tif" or DataType=="bmp" or DataType=="png" \
       or DataType=="jpg" or DataType=="gif" or DataType=="grd"  or DataType=="raw":
       return 1
    else:
        return 0

#==========================main函数=============================================   
if __name__ =='__main__':
    #SuperMap.Init()
    if len(sys.argv)==8:
        #============输入参数================
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
            print "打开数据源成功"
            #判断数据类型是否是文件型数据，文件型的传文件夹（包括gdb）
            if fType=="AIBinCov" or fType=="GDBVector" :
                SuperMap.SetUseFME(True)
                if fType=="GDBRaster":                     
                    b=SuperMap.ImportRasterFile(odsAlias, "", "encNONE", fileType, DataPath,importMode)
                else:
                    b=SuperMap.ImportVectorFile(odsAlias, "", "encNONE", fileType, DataPath,importMode)
                if b:
                    print fType+"导入成功"
                else:
                    print fType+"导入失败"
                    
            else: 
                bVisi=Visit(DataPath)
                if IsRaster:                
                    UGOImportRaster(DataPath,bUserFME,bVisi)
                else:                
                    UGOImportVector(DataPath,bUserFME,bVisi)
        else:
            print "打开数据源失败"
        SuperMap.Exit()#清空环境，释放内存
    else:        
        print "输入参数错误!"
        print "============请按顺序输入:================"
        print "1.脚本\n2.UGO Bin\n3.数据路径\n4.数据源路径(server)\n5.数据源(User)"
        print "6.数据源(Pwd)\n7.引擎类型（sceSDBPlus/sceUDB/sceOraclePlus)\n8.导入数据类型(区分大小写)"
        print "=========================================="
