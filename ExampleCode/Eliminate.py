# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\地图综合.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
	if bOpen == 1:
		dtSrc = 'county'
		SuperMap.Eliminate(odsAlias, dtSrc, 134591789, 0, 1, 0)
		SuperMap.CloseDataSource(odsAlias)	
	else:
		print "打开数据源失败！"
	SuperMap.Exit()#清空组件环境释放内存
