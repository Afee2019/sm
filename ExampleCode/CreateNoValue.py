# coding: GB2312

import sys
sys.path.append(r'D:\DotNetPythonBin\Bin')
import string
import re
import smu as SuperMap
import os
import time
SuperMap.Init()


#=====================================
#��Ҫ�޸ĵĲ���
server="sfc60"
user="testMTT"
pwd="testMTT"
dtName="UGCIMAGE_TF"
reMatch = '{\d\D}.tif'   
testPath=r"F:\2012\python��������\Data\AppendRasterFile"
fileType = "fileTIF"
imageTpye='IPF_RGB'
odsAlias="oracle"
fileClass='.tif' #Ӱ���ļ���׺
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


#����׺��ΪfileClass���ļ����浽һ��������    
for root, dirs, files in os.walk(testPath):
        for file in files:
                ext = os.path.splitext(file)[1]
                if (ext== fileClass):
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
    bCreate = SuperMap.CreateDatasetRaster(odsAlias,dtName, 'Image', 'encLZW',imageTpye,nWidth,nHeight, dLeft, dTop,dRight,dBottom,256,0)
   

SuperMap.Exit()#��ջ������ͷ��ڴ�
