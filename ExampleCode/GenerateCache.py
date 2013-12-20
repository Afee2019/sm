# --*-- coding: cp936 --*--
import os, sys
ugo=r'G:\01_SourceCode_7.0.0_B\Builds\Win_Solution_vc11\BinD_Unicode'
sys.path.append(ugo)

import smu
import string

def main(wkspc, map, sci, Outpath,Scale, Left, Top, Right, Bottom):
	smu.GenerateCache(wkspc, map, sci,Outpath, Scale, Left,Top ,Right,Bottom)


if __name__ == '__main__':
	if len(sys.argv)==10:
		wkspc = sys.argv[1]
		map = sys.argv[2]
		sci = sys.argv[3]
		Outpath = sys.argv[4]
		Scale = string.atof(sys.argv[5])
		left = string.atof(sys.argv[6])
		top = string.atof(sys.argv[7])
		right = string.atof(sys.argv[8])
		bottom = string.atof(sys.argv[9])
		main(wkspc, map, sci, Outpath, Scale, left, top, right, bottom)
