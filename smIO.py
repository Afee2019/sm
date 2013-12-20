#coding: gb2312
#DataProcessing
#���ݴ���ķ����ŵ�����ļ���

import smBase as py
import filetk as tk

class DataPump:
    def __init__(self):
        self.bOK = 0

    #Sample: ImportGrids('D:\\Data\\SRTM', '.*.tif', 'D:\\Data\\UDB', 'encLZW', 'fileTIF')
    def ImportGrids(self, srcPath, reMatch, destPath, encType, fileType):
        #��ȡ�ļ�����Ҫ������ļ����б������fl.FileLists��
        fl = tk.Folder(srcPath)
        fl.reMatch = reMatch
        fl.GetFileLists()

        #�����
        for file in fl.FileLists:
            #����UDB����Դ
            nds = py.uds(destPath+'\\'+file[-14:-4]+'.udb', 'udbAlias');
            nds.Create()
            nds.ImportGrid(file[-14:-4],encType, fileType, file)
            nds.Close()






