# coding: GB2312

import sys
sys.path.append(r'E:\Develop\UGO6.1\01_SourceCode\Builds\Win_Solution_vc9\Bin')
import string
import re
import smu as SuperMap
import os
import time
SuperMap.Init()


#=====================================
#��Ҫ�޸ĵĲ���
server="ora9"
user="ora9"
pwd="ora9"
dtName="test"
reMatch = '[\d\D]*.img'   
testPath=r"F:\Temp\�½��ļ��� (2)"
fileType = "fileIMG"
imageTpye='IPF_BYTE'
odsAlias="oracle"
logfilename = "c:/Test.log"#��־�ļ�·��
#��Ҫ�޸ĵĲ���
#=====================================
def WriteLog(tmpstr):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S	",time.localtime())
    logstr = str(tmpstr) + time_str +'\n'
    print(logstr)
    f = open(logfilename,"a")
    f.write(logstr)
    f.close()


datafiles = []
left=[]
top=[]
right=[]
bottom=[]
ratiox=[]
ratioy=[]
L=[]


#ƥ��������ʽ������������append��datafiles������׷��    
for root, dirs, files in os.walk(testPath):
    for file in files:
        if (re.match(reMatch,file)):
            datafiles.append(os.path.join(root, file))
                        
#��ȡÿ��Ӱ���ļ������ҵ���Χ�����浽����
for file in datafiles:
	L= SuperMap.GetImageGeoRef(fileType,file)
	print L
	l=float(L[0][0])
	t=float(L[0][1])
	r=float(L[0][2])
	b=float(L[0][3])
	w=int(L[1][0])
	h=int(L[1][1])
	x=(r-l)/w
	y=(t-b)/h
				
	left.append(l)
	right.append(r)
	top.append(t)
	bottom.append(b)
	ratiox.append(x)
	ratioy.append(y)

#��ȡ�������±߽�
print left
dLeft=min(left)
dRight=max(right)
dTop=max(top)
dBottom=min(bottom)

#��ȡ�ֱ��ʣ�Ӱ����С�ֱ�����Ϊ���ݼ��ֱ���
dRatioX = min(ratiox)
dRatioY = min(ratioy)

#����Ӱ�����ݼ���Ⱥ͸߶�
nWidth = int((dRight-dLeft)/dRatioX)
nHeight=int((dTop-dBottom)/dRatioY)

#���¼��㣬��֤�ֱ�����ȷ
dRight=dLeft+dRatioX*nWidth
dBottom=dTop-dRatioY*nHeight
isOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)
#����Դ�򿪳ɹ�������в��������ӡ��Ϣ�˳�
if isOpen == 1:
    SuperMap.DeleteDataset (odsAlias,dtName)
    WriteLog("�������ݼ���ʼ")
    bCreate = SuperMap.CreateDatasetRaster(odsAlias,dtName, 'Image', 'encLZW',imageTpye,nWidth,nHeight, dLeft, dTop,dRight,dBottom,256)
    WriteLog("�������ݼ�����")
    if bCreate == 1:
        WriteLog("UGC׷�����ݼ���ʼ")
        n=len(datafiles)
        T1 = "T1"
        for i in range(0,n):
                print i
                print odsAlias,dtName,fileType,datafiles[i]
                bAppend=SuperMap.AppendRasterFileIgnoreBorderValue(odsAlias,dtName,fileType,datafiles[i],0)
                if bAppend==1:
                    print "׷�ӳɹ�"
                else:
                    print "׷��ʧ��"
        WriteLog("UGC׷�����ݼ�����")
    else:
        print "�½����ݼ�ʧ�ܣ�"
    SuperMap.CloseDataSource(odsAlias)
else:
    print "������Դʧ�ܣ�"

SuperMap.Exit()#��ջ������ͷ��ڴ�
