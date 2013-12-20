#coding: gb2312
#�����࣬����Դ�����ݼ��������ռ�ȶ���ŵ�����

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
        self.area = self.width*self.height              #���
        self.length = 2*(self.width+self.height)        #�ܳ�

#դ���ļ���Ϣ
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



#���ݼ��Ļ���
class dt:
    def __init__(self, ds, name = ''):
        self.ds = ds
        self.name = name



#����Դ����
class ds:
    def __init__(self, alias='ds'):
        self.alias = alias
        self.bOpened = 0
        self.nDtCount = 0
        self.Dts = []
        self.DtNames = []
        self.type = 'sceUDB'

    #�ر�����Դ
    def Close(self):
        smu.CloseDataSource(self.alias)
        self.bOpened = 0
        self.nDtCount = 0
        self.Dts = []

    #����ʸ�����ݼ�
    #dtType��ѡֵ�� Tabular, Point, Line, Region, Text, NetWork, CAD
    #encType��ѡֵ�� encNONE, encByte, encWORD, encTBYTE, encDWORD, encFLOAT
    def CreateVector(self, dtName, dtType, encType):
        return 0


    #����դ�����ݼ���ָ������Χ�ͷֱ��ʣ�
    #dtType, ���ݼ����ͣ���ѡֵ��Image; DEM; GRID 
    #encType�����루ѹ�������ͣ���ѡֵ�� encNONE; encDCT; encSGL; encLZW; encCompound
    #pixFormat�����ظ�ʽ�� ��ѡֵ��
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
    #iBlkSize, Ӱ����С����ѡֵ��64�� 128�� 256�� 512�� 1024�� 2048�� 4096�� 8192
    #dLeft,
    #dTop,
    #dRight, 
    #dBottom,
    #dResX,
    #dResY,
    #nBandCount, ��������Ĭ��Ϊ1
    #����ds.CreateRaster('RasterDt', 'Image', 'encDCT', 'IPF_RGB', 256, 71.1, 52.7, 133.5, 14.7, 0.000083, 0.000083)
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

    #����դ�����ݼ���ָ������Χ�Ϳ��ߣ�
    #dtType, ���ݼ����ͣ���ѡֵ��Image; DEM; GRID 
    #encType�����루ѹ�������ͣ���ѡֵ�� encNONE; encDCT; encSGL; encLZW; encCompound
    #pixFormat�����ظ�ʽ�� ��ѡֵ��
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
    #iBlkSize, Ӱ����С����ѡֵ��64�� 128�� 256�� 512�� 1024�� 2048�� 4096�� 8192
    #dLeft,
    #dTop,
    #dRight, 
    #dBottom,
    #iWidth, դ�����ݼ���ȣ���λ������
    #iHeight, դ�����ݼ��߶ȣ���λ������
    #nBandCount, ��������Ĭ��Ϊ1
    #����ds.CreateRaster('RasterDt', 'Image', 'encDCT', 'IPF_RGB', 256, 71.1, 52.7, 133.5, 14.7, 70000, 80000)
    def CreateRaster2(self, dtName, dtType, encType, pixFormat, iBlkSize, dLeft, dTop, dRight, dBottom, iWidth, iHeight, nBandCount = 1):
        if smu.CreateDatasetRaster(self.alias, dtName, dtType, encType,pixFormat, iWidth, iHeight, dLeft, dTop, dRight, dBottom, iBlkSize, nBandCount):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False


    #ɾ�����ݼ�
    #dtName, ���ݼ���
    def DeleteDataset(self, dtName):
        return smu.DeleteDataset(self.alias, dtName)

    #��׷�ӵķ�ʽ����Ӱ�����ݼ�
    # dtName, 
    # imgType, 
    # fileName,
    #Sample: 
    def AppendRasterFile(self, dtName, imgType, fileName):
        return smu.AppendRasterFile(self.alias, dtName, imgType, fileName)

    #��׷�ӵķ�ʽ����Ӱ�����ݼ�
    # dtName, 
    # imgType, 
    # fileName,
    # dColor,
    #Sample: 
    def AppendRasterFileIgnoreValue(self, dtName, imgType, fileName,dColor):
        return smu.AppendRasterFileIgnoreColor(self.alias, dtName, imgType, fileName,dColor)



    #��GRID��ʽ����դ������Ϊ�����ݼ�
    #dtName -- ���������ݼ�������
    #encType -- �����ݼ���������
    #fileType -- դ���ļ�������
    #fileName -- դ���ļ���ȫ·�����ļ���
    def ImportGrid(self, dtName, encType, fileType, fileName):
        if smu.ImportRasterFile(self.alias, dtName,encType,fileType, fileName,1):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False

    #��Image��ʽ����դ������
    def ImportImage(self, dtName, encType, fileType, fileName):
        #���һ��������־�Ƿ���ΪGRID���ͣ�1 -- Is Grid�� 0 -- Is not GRID
        if smu.ImportRasterFile(self.alias, dtName,encType,fileType, fileName,0):
            self.nDtCount = self.nDtCount+1
            self.DtNames.append(dtName)
            self.Dts.append(dt(self, dtName))
            return True
        return False

        
#UDB���͵�����Դ
class uds(ds):

    #��fileName��Ϊ''�������ڴ�ģʽ
    def __init__(self, fileName, alias = 'ds'):
        ds.__init__(self,alias)
        self.type = 'sceUDB'
        self.fileName = fileName

        
    #������Դ����fileNameΪ''����Ϊ�ڴ�ģʽ
    def Open(self):
        self.bOpened = smu.OpenDataSource(self.fileName, "", "", self.type, self.alias)
        self.nDtCount = smu.GetDatasetCount(self.alias)
        self.DtNames = list(smu.GetAllDatasetName(self.alias))
        self.Dts = []
        for dtName in self.DtNames:
            self.Dts.append(dt(self, dtName))

        return self.bOpened

    #��������Դ����fileNameΪ'', ��Ϊ�ڴ�ģʽ
    def Create(self):
        #���ļ��Ѵ��ڣ���ɾ��ԭ�ļ�
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

#������һЩͨ�õĺ���

#��ȡָ����դ���ļ�����Ϣ
def GetImgFileInfo(fileName):
    imgInfo = imgFileInfo()
    imgInfo.fileName = fileName
    L = smu.GetImageGeoRef(imgInfo.imgType,fileName)
    imgInfo.bounds = rect(L[0][0], L[0][1],L[0][2],L[0][3])
    imgInfo.width = L[1][0];
    imgInfo.height = L[1][1];

    


