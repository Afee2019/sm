# --*-- coding: cp936 --*--
import os, sys
ugo=r'G:\01_SourceCode_7.0.0_B\Builds\Win_Solution_vc11\BinD_Unicode'
sys.path.append(ugo)
#C:\Python27\python E:\2012-02-20\OBJN-759\GetDatasetInfo.py 
#"E:\2012-02-20\2013-07-29\data3\test.udb" "" "" "sceUDB" "aaa" "test"

import smu
import string

def main(Server, User, Password, Engtype, odsAlias, dtNmae):
	isOpen=smu.OpenDataSource(Server,User,Password, Engtype, odsAlias)
	info = smu.GetDatasetInfo(odsAlias, dtNmae)
	print info[0][0]
	print info[1][0]
	print info[1][1]
	print info[1][2]
	print info[1][3]
	
if __name__ == '__main__':
	if len(sys.argv)==7:
		Server = sys.argv[1]
		User = sys.argv[2]
		Password = sys.argv[3]
		Engtype = sys.argv[4]
		odsAlias = sys.argv[5]
		dtNmae = sys.argv[6]
		main(Server, User, Password, Engtype, odsAlias, dtNmae)
