#coding: gb2312
#������(smBase)�Ĳ��Դ���
import os
import sm.smBase as sm

#�Ȳ���UDB����Դ
fileName = r'C:\test\test.udb'
uddFileName = r'C:\test\test.udd'

if os.path.exists(fileName):
    os.remove(fileName)
if os.path.exists(uddFileName):
    os.remove(uddFileName)

uds = sm.uds(fileName, 'uds')
uds.Create()
uds.CreateRaster('HeBeiRaster', 'Image', 'encLZW', 'IPF_RGB', 512, 114.249, 39.8751, 118.75, 39.833, 0.0000055555555555555558, 0.0000055555555555555558)
uds.AppendRasterFile('HeBeiRaster', 'fileTIF', 'C:\\work\\��Ŀ\\��������\\orig\\J50G004005.tif')
uds.AppendRasterFile('HeBeiRaster', 'fileTIF', 'C:\\work\\��Ŀ\\��������\\orig\\J50G004076.tif')
uds.Close()








#�ٲ����ڴ�����Դ




