# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·�����ӵ���������
import smu as sm #����SuperMapģ��

sm.Init()#��ʼ��Python�������;

#====================================
#��Ҫ�޸ĵĲ���
server=r"F:\Temp\2012-08-25\����3.sdb" 
user=""
pwd=""
odsAlias="odsAlias"
#====================================

def Buffer(dsSrc, dtSrc, dsDst, dtDst, dDistance,strUnit, iUnion, iSegment):
	sm.Buffer(dsSrc, dtSrc, dsDst, dtDst, dDistance, 
			dDistance, strUnit, 'Round', iUnion, iSegment)

def BufferLine(dsSrc, dtSrc, dsDst, dtDst, dLeft, dRight, strUnit, 
		strEndType, iUnion, iSegment):
	sm.Buffer(dsSrc, dtSrc, dsDst, dtDst, dLeft, dRight, 
		strUnit, strEndType, iUnion, iSegment)


if __name__ == '__main__':
	bOpen=sm.OpenDataSource(server,user, pwd,"sceSDBPlus",odsAlias)#��oracle����Դ
	if bOpen == 1:
		dtSrc = '����'
		dtDst = '����buf'
		strUnit = 'Meter'
		sm.DeleteDataset(odsAlias, dtDst)
		strDtType = sm.GetDatasetType(odsAlias, dtSrc)

		if strDtType.find('Point')!=-1 or strDtType.find('Region')!=-1:
			print strDtType
			Buffer(odsAlias, dtSrc, odsAlias, dtDst, 10, strUnit, 0, 12)
		elif strDtType.find('')!=-1:
			BufferLine(odsAlias, dtSrc, odsAlias, dtDst, 10, 10,
					strUnit, 'Flat', 0, 100)
		
		sm.CloseDataSource(odsAlias)	
	else:
		print "������Դʧ�ܣ�"
	sm.Exit()#�����������ͷ��ڴ�