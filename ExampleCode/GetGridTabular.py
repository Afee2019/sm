# coding: GB2312
#===================================
#===================================
import os
import sys
sys.path.append(r"E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\BinD") #��.net�����·����ӵ���������
import smu #����SuperMapģ��


#====================================
#��Ҫ�޸ĵĲ�������Oracle����ԴΪ��
server="F:\����2012\������������Ҫ������ļ�\����ļ���\A04040500.udb" 
user=""
pwd=""
odsAlias=""
dtName=""
#====================================

smu.Init()#��ʼ��Python�������;
bOpen=smu.OpenDataSource(server,user, pwd,"sceUDB",odsAlias)#��oracle����Դ
if bOpen == 1:
	smu.DeleteDataset(odsAlias, 'vat')
	bBuild=smu.GetGridTabular(odsAlias,'tt','vat')
	if bBuild == 1:
		print "��ȡդ�����Ա�ɹ�"
	else:
		print "��ȡդ�����Ա�ʧ��"
	smu.CloseDataSource(odsAlias)
else:
	print "������Դʧ�ܣ�"

smu.Exit()#�����������ͷ��ڴ�
