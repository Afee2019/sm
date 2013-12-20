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
dtName="UpdatePyramidByBound"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    dLeft=0
    dTop=1537
    dRight=1728
    dBottom=0
    bBuild=SuperMap.UpdatePyramidByBound(odsAlias,dtName,dLeft,dTop,dRight,dBottom)#创建影像金字塔
    if bBuild == 1:
        print "更新影像金字塔成功！"
    else:
        print "更新影像金字塔失败！"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"

SuperMap.Exit()#清空组件环境释放内存
