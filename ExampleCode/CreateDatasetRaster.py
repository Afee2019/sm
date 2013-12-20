# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"D:\DotNetPythonBin\Bin") #将.net组件的路径添加到环境变量
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数，以Oracle数据源为例
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

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    bCreate=SuperMap.CreateDatasetRaster(odsAlias,dtName,strType,strEncType,strPixfmt,
                                        iWidth,iHeight,dLeft,dTop,dRight,dBottom,iBlkSize)
    if bCreate == 1:
        print "创建栅格数据集成功"
    else:
        print "创建栅格数据集失败"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"
    
SuperMap.Exit()#清空组件环境释放内存
