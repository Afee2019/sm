# coding: GB2312
#===================================
#��ָ�������ݼ�׷�����ݼ�
#AppendDatasetRaster 	
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu as SuperMap #����SuperMapģ��

SuperMap.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
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
	bOpen=SuperMap.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtVector = 'VectorResult'
		dtRaster = 'contour_raster'
		strFieldName = 'ResultField'
		SuperMap.DeleteDataset(odsAlias, dtVector)
		RasterToLine(odsAlias, dtRaster, odsAlias, dtVector, strFieldName, 
				0, 0, 0, 0, 2, -9999, 0, 1)
		SuperMap.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	SuperMap.Exit()#�����������ͷ��ڴ�
