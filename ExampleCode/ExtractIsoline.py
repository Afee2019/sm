# coding: GB2312
#===================================
#向指定的数据集追加数据集
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"G:\01_SourceCode_7.0.0_B\Builds\Win_Solution_vc11\BinD_Unicode") #将.net组件的路径添加到环境变量
import smu as SuperMap #导入SuperMap模块

SuperMap.Init()#初始化Python组件环境;

#====================================
#需要修改的参数
server=r"E:\2012-02-20\2013-07-29\eeeeeee.udb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================


if __name__ == '__main__':
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceUDB",odsAlias)#打开oracle数据源
	if bOpen == 1:
		dtGrid1 = 'srtm_01_02_1'
		dtGrid2 = 'DemData'
		#SuperMap.DeleteDataset(odsAlias, dtGrid2)
		L = SuperMap.ExtractIsoline(odsAlias, dtGrid1, 0,100,3,0,0,odsAlias, dtGrid2,"asdfa")
		print L
		SuperMap.CloseDataSource(odsAlias)	
	else:
		print "打开数据源失败！"
	SuperMap.Exit()#清空组件环境释放内存
