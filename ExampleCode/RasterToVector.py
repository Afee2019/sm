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
server=r"F:\Temp\2012-08-25\rvconversion.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

def RasterToLine(dsSrc, dtRaster, dsDst, dtVector, strFieldName, iUseValue, dValue, 
		dValueTolerence, iSmooth, iSmoothDegree,iNoData, iNoDataTolerence, iThin):

	SuperMap.RasterToVector(dsSrc, dtRaster, dsDst, dtVector, 'Line',
			strFieldName, iUseValue, dValue, dValueTolerence, 
			iSmooth, iSmoothDegree,iNoData, iNoDataTolerence, iThin)

def RasterToRegion(dsSrc, dtRaster, dsDst, dtVector, strFieldName, iUseValue, dValue, 
		dValueTolerence,iNoData, iNoDataTolerence, iThin):

	SuperMap.RasterToVector(dsSrc, dtRaster, dsDst, dtVector, 'Region',
			strFieldName, iUseValue, dValue, dValueTolerence,
			0, 0, iNoData, iNoDataTolerence, 0)

def RasterToPoint(dsSrc, dtRaster, dsDst, dtVector, strFieldName, iUseValue, dValue, 
		dValueTolerence, iNoData, iNoDataTolerence):

	SuperMap.RasterToVector(dsSrc, dtRaster, dsDst, dtVector, 'Point',
			strFieldName, iUseValue, dValue, dValueTolerence,
			0, 0, iNoData, iNoDataTolerence, 0)


if __name__ == '__main__':
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
	if bOpen == 1:
		dtVector = 'VectorResult'
		dtRaster = 'contour_raster'
		strFieldName = 'ResultField'
		SuperMap.DeleteDataset(odsAlias, dtVector)
		RasterToLine(odsAlias, dtRaster, odsAlias, dtVector, strFieldName, 
				0, 0, 0, 0, 2, -9999, 0, 1)
		SuperMap.CloseDataSource(odsAlias)	
	else:
		print "打开数据源失败！"
	SuperMap.Exit()#清空组件环境释放内存
