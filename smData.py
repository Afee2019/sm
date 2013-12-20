#coding: gb2312
#基础类，数据源、数据集、工作空间等对象放到这里

import os
import sys
import math
sys.path.append(r"C:\Python27\Bin_Unicode_x64")

import smBase
import smu
smu.Init()



#Rect2D
class rect:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right= right
        self.bottom = bottom
        self.width = right-left
        self.height = top-bottom
        self.area = self.width*self.height              #面积
        self.length = 2*(self.width+self.height)        #周长

#栅格文件信息
class imgFileInfo:
    def __init__(self):
        self.fileName = ''
        self.bounds = rect(0.0, 0.0, 0.0, 0.0)
        self.imgType = 'fileTIF'
        self.bandCount = 1
        self.resX = 1.0
        self.resY = 1.0
        self.width = 0
        self.height = 0



#数据集的基类
class dt:
    def __init__(self, ds, name = ''):
        self.ds = ds
        self.name = name



#数据源基类
class ds:
    def __init__(self, alias='ds'):
        self.alias = alias
        self.bOpened = 0
        self.nDtCount = 0
        self.Dts = []
        self.DtNames = []
        self.type = 'sceUDB'

    #关闭数据源
    def Close(self):
        smu.CloseDataSource(self.alias)
        self.bOpened = 0
        self.nDtCount = 0
        self.Dts = []

    #创建矢量数据集
    #dtType可选值： Tabular, Point, Line, Region, Text, NetWork, CAD
    #encType可选值： encNONE, encByte, encWORD, encTBYTE, encDWORD, encFLOAT
    def CreateVector(self, dtName, dtType, encType):
        return 0


    #创建栅格数据集（指定地理范围和分辨率）
    #dtType, 数据集类型，可选值：Image; DEM; GRID 
    #encType，编码（压缩）类型，可选值： encNONE; encDCT; encSGL; encLZW; encCompound
    #pixFormat，像素格式， 可选值：
    #   IPF_MONO; 
    #   IPF_FBIT; 
    #   IPF_UBYTE; 
    #   IPF_BYTE; 
    #   IPF_TBYTE; 
    #   IPF_UTBYTE; 
    #   IPF_RGB; 
    #   IPF_RGBA; 
    #   IPF_TRGB; 
    #   IPF_LONG; 
    #   IPF_ULONG; 
    #   IPF_LONGLONG; 
    #   IPF_FLOAT; 
    #   IPF_DOUBLE;
    #iBlkSize, 影像块大小，可选值：64， 128， 256， 512， 1024， 2048， 4096， 8192
    #dLeft,
    #dTop,
    #dRight, 
    #dBottom,
    #dResX,
    #dResY,
    #nBandCount, 波段数，默认为1
    #例：ds.CreateRaster('RasterDt', 'Image', 'encDCT', 'IPF_RGB', 256, 71.1, 52.7, 133.5, 14.7, 0.000083, 0.000083)
    def CreateRaster(self, dtName, dtType, encType, pixFormat, iBlkSize, dLeft, dTop, dRight, dBottom, dResX, dResY, nBandCount = 1):
        iWidth = int(math.ceil(float(dRight-dLeft)/float(dResX)))
        iHeight = int(math.ceil(float(dTop-dBottom)/float(dResY)))
        dRight = dLeft+iWidth*dResX
        dBottom = dTop-iHeight*dResY
        if smu.CreateDatasetRaster(self.alias, dtName, dtType, encType,pixFormat, iWidth, iHeight, dLeft, dTop, dRight, dBottom, iBlkSize, nBandCount):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False

    #创建栅格数据集（指定地理范围和宽、高）
    #dtType, 数据集类型，可选值：Image; DEM; GRID 
    #encType，编码（压缩）类型，可选值： encNONE; encDCT; encSGL; encLZW; encCompound
    #pixFormat，像素格式， 可选值：
    #   IPF_MONO; 
    #   IPF_FBIT; 
    #   IPF_UBYTE; 
    #   IPF_BYTE; 
    #   IPF_TBYTE; 
    #   IPF_UTBYTE; 
    #   IPF_RGB; 
    #   IPF_RGBA; 
    #   IPF_TRGB; 
    #   IPF_LONG; 
    #   IPF_ULONG; 
    #   IPF_LONGLONG; 
    #   IPF_FLOAT; 
    #   IPF_DOUBLE;
    #iBlkSize, 影像块大小，可选值：64， 128， 256， 512， 1024， 2048， 4096， 8192
    #dLeft,
    #dTop,
    #dRight, 
    #dBottom,
    #iWidth, 栅格数据集宽度，单位：像素
    #iHeight, 栅格数据集高度，单位：像素
    #nBandCount, 波段数，默认为1
    #例：ds.CreateRaster('RasterDt', 'Image', 'encDCT', 'IPF_RGB', 256, 71.1, 52.7, 133.5, 14.7, 70000, 80000)
    def CreateRaster2(self, dtName, dtType, encType, pixFormat, iBlkSize, dLeft, dTop, dRight, dBottom, iWidth, iHeight, nBandCount = 1):
        if smu.CreateDatasetRaster(self.alias, dtName, dtType, encType,pixFormat, iWidth, iHeight, dLeft, dTop, dRight, dBottom, iBlkSize, nBandCount):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False


    #删除数据集
    #dtName, 数据集名
    def DeleteDataset(self, dtName):
        return smu.DeleteDataset(self.alias, dtName)

    #以追加的方式导入影像数据集
    # dtName, 
    # imgType, 
    # fileName,
    #Sample: 
    def AppendRasterFile(self, dtName, imgType, fileName):
        return smu.AppendRasterFile(self.alias, dtName, imgType, fileName)

    #以追加的方式导入影像数据集
    # dtName, 
    # imgType, 
    # fileName,
    # dColor,
    #Sample: 
    def AppendRasterFileIgnoreValue(self, dtName, imgType, fileName,dColor):
        return smu.AppendRasterFileIgnoreColor(self.alias, dtName, imgType, fileName,dColor)



    #以GRID方式导入栅格数据为新数据集
    #dtName -- 新生成数据集的名字
    #encType -- 新数据集编码类型
    #fileType -- 栅格文件的类型
    #fileName -- 栅格文件的全路径及文件名
    def ImportGrid(self, dtName, encType, fileType, fileName):
        if smu.ImportRasterFile(self.alias, dtName,encType,fileType, fileName,1):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False

    #以Image方式导入栅格数据
    def ImportImage(self, dtName, encType, fileType, fileName):
        #最后一个参数标志是否导入为GRID类型，1 -- Is Grid， 0 -- Is not GRID
        if smu.ImportRasterFile(self.alias, dtName,encType,fileType, fileName,0):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False

        
#UDB类型的数据源
class uds(ds):

    #若fileName设为''，则是内存模式
    def __init__(self, fileName, alias = 'ds'):
        ds.__init__(self,alias)
        self.type = 'sceUDB'
        self.fileName = fileName

        
    #打开数据源，若fileName为''，则为内存模式
    def Open(self):
        self.bOpened = smu.OpenDataSource(self.fileName, "", "", self.type, self.alias)
        self.nDtCount = smu.GetDatasetCount(self.alias)
        self.DtNames = list(smu.GetAllDatasetName(self.alias))
        self.Dts = []
        for dtName in self.DtNames:
            self.Dts.append(dt(self, dtName))

        return self.bOpened

    #创建数据源，若fileName为'', 则为内存模式
    def Create(self):
        #若文件已存在，则删除原文件
        if len(self.fileName)>0:
            uddFile = self.fileName.split('.')[0]+'.udd'
            if os.path.exists(self.fileName):
                os.remove(self.fileName)
            if os.path.exists(uddFile):
                os.remove(uddFile)

        self.bOpened = smu.CreateDataSource(self.fileName, "", "", self.type, self.alias)
        self.nDtCount = 0
        self.DtNames = []
        self.Dts = []
        
        return self.bOpened

#下面是一些通用的函数

#获取指定的栅格文件的信息
def GetImgFileInfo(fileName):
    imgInfo = imgFileInfo()
    imgInfo.fileName = fileName
    L = smu.GetImageGeoRef(imgInfo.imgType,fileName)
    imgInfo.bounds = rect(L[0][0], L[0][1],L[0][2],L[0][3])
    imgInfo.width = L[1][0];
    imgInfo.height = L[1][1];

    


