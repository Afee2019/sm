# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·�����ӵ���������
import smu as sm #����SuperMapģ��



if __name__ == '__main__':
	sm.Init()#��ʼ��Python�������;

	bResult = sm.ExportMapToFile(r'F:\Temp\2012-08-25\test.smwu', 'test', 'fileTIF', r'F:\Temp\2012-08-25\test.tif')
	if bResult == 1:
		print '�����ɹ�.'
	else:
		print "����ʧ��."
	sm.Exit()#�����������ͷ��ڴ�