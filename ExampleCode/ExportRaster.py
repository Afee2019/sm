# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu as sm #导入SuperMap模块

sm.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"F:\Temp\2012-08-25\表面分析.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
	if bOpen == 1:
		dtGrid1 = 'Dem2'
		sm.ExportRaster(odsAlias, dtGrid1, 'fileTIF', r'F:\Temp\2012-08-25\test.tif')
		sm.CloseDataSource(odsAlias)	
	else:
		print "打开数据源失败！"
	sm.Exit()#清空组件环境释放内存
