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
server=r"F:\Temp\2012-08-25\辽宁3.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

def Buffer(dsSrc, dtSrc, dsDst, dtDst, strUint, strR,  iUnion, iSegment, iRing):
	sm.BufferMulti(dsSrc, dtSrc, dsDst, dtDst, strUnit, 'Round', strR, 0, iUnion, iSegment, iRing)

def BufferLine(dsSrc, dtSrc, dsDst, dtDst, strUnit, strEndType, strR, iLeftSide, iUnion, iSegment, iRing):
	sm.BufferMulti(dsSrc, dtSrc, dsDst, dtDst, strUnit, strEndType, strR, 
			iLeftSide, iUnion, iSegment, iRing)


if __name__ == '__main__':
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#打开oracle数据源
	if bOpen == 1:
		dtSrc = '国道'
		dtDst = '国道buf'
		strUnit = 'Meter'
		sm.DeleteDataset(odsAlias, dtDst)
		strDtType = sm.GetDatasetType(odsAlias, dtSrc)

		if strDtType.lower()=='point' or strDtType.lower()=='region':
			print strDtType
			Buffer(odsAlias, dtSrc, odsAlias, dtDst, strUnit,
					'30,45, 56', 0, 12, 1)
		elif strDtType.lower()=='line':
			BufferLine(odsAlias, dtSrc, odsAlias, dtDst, strUnit,
					'Flat', '30,45,56',1, 0,100, 1)
		
		sm.CloseDataSource(odsAlias)	
	else:
		print "打开数据源失败！"
	sm.Exit()#清空组件环境释放内存
