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
#需要修改的参数
server="sfc60"
user="testMTT"
pwd="testMTT"
dtName="UGCIMAGE_TF"
reMatch = '{\d\D}.tif'   
testPath=r"F:\2012\python范例程序\Data\AppendRasterFile"
fileType = "fileTIF"
imageTpye='IPF_RGB'
odsAlias="oracle"
fileClass='.tif' #影像文件后缀
logfilename = "c:/Test.log"#日志文件路径
#需要修改的参数
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


#将后缀名为fileClass的文件保存到一个数组里    
for root, dirs, files in os.walk(testPath):
        for file in files:
                ext = os.path.splitext(file)[1]
                if (ext== fileClass):
                        datafiles.append(os.path.join(root, file))
                        
#获取每个影像文件的左右地理范围，保存到数组
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

#获取左右上下边界
print left
dLeft=min(left)
dRight=max(right)
dTop=max(top)
dBottom=min(bottom)

#获取分辨率，影像最小分辨率作为数据集分辨率
dRatioX = min(ratiox)
dRatioY = min(ratioy)

#计算影像数据集宽度和高度
nWidth = int((dRight-dLeft)/dRatioX)
nHeight=int((dTop-dBottom)/dRatioY)

#重新计算，保证分辨率正确
dRight=dLeft+dRatioX*nWidth
dBottom=dTop-dRatioY*nHeight
isOpen=SuperMap.OpenDataSource(server,user, pwd,"sceOraclePlus",odsAlias)
#数据源打开成功，则进行操作否则打印消息退出
if isOpen == 1:
    SuperMap.DeleteDataset (odsAlias,dtName)
    WriteLog("创建数据集开始")
    bCreate = SuperMap.CreateDatasetRaster(odsAlias,dtName, 'Image', 'encLZW',imageTpye,nWidth,nHeight, dLeft, dTop,dRight,dBottom,256,0)
   

SuperMap.Exit()#清空环境，释放内存
