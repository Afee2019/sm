# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #将.net组件的路径添加到环境变量
import smu #导入SuperMap模块


#====================================
#需要修改的参数，以Oracle数据源为例
server="F:\测评2012\测试软件会议纪要及相关文件\结果文件夹\A04040500.udb" 
user=""
pwd=""
odsAlias=""
dtName=""
#====================================

smu.Init()#初始化Python组件环境;
bOpen=smu.OpenDataSource(server,user, pwd,"sceUDB",odsAlias)#打开oracle数据源
if bOpen == 1:
	smu.DeleteDataset(odsAlias, 'vat')
	bBuild=smu.GetGridTabular(odsAlias,'tt','vat')
	if bBuild == 1:
		print "获取栅格属性表成功"
	else:
		print "获取栅格属性表失败"
	smu.CloseDataSource(odsAlias)
else:
	print "打开数据源失败！"

smu.Exit()#清空组件环境释放内存
