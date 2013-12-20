# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\Bin") #将.net组件的路径添加到环境变量
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数，以Oracle数据源为例
server="cp1" 
user="cqff48"
pwd="cqff48"
odsAlias="oracle"
#====================================

bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)#打开oracle数据源
if bOpen == 1:
    SuperMap.DeleteDataset(odsAlias, 'wayptP')
    bCreate=SuperMap.CreateDatasetGroup(odsAlias)
    if bCreate == 1:
        print "新建数据集集合成功"
    else:
        print "新建数据集集合失败！"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "打开数据源失败！"
    
SuperMap.Exit()#清空组件环境释放内存
