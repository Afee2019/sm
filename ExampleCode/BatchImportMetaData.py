# --*-- coding:cp936 --*--

import sys, os
sys.path.append(r'E:\Develop\UGO6.1\Builds\Win_Solution_vc9\BinD')
import smu as SuperMap

server='cp1'
user='dlgff'
pwd='dlgff'
engType='sceOraclePlus'
metaData=r'E:\工作\2012\2012-08\2012-08-02\MetadataImport\25meta\25meta'

#SuperMap.DropMetaDatabase(server, user, pwd, engType)
#SuperMap.CreateMetaDatabase(server, user, pwd, engType)
SuperMap.BatchImportMetaData(server, user, pwd, engType, 1, metaData)

