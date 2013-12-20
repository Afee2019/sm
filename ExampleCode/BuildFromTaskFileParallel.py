# --*-- coding: cp936 --*--
import os, sys, time
import subprocess

# 多进程并行执行切图
def parallel(wkspc, map, dir, scis):
	pl = []
	for sci in scis:
		args = 'python BuildFromTaskFile.py %s %s %s %s' %(wkspc, map, dir, sci)
		print args
		p = subprocess.Popen(args, stdout=None)
		pl.append(p)

def findsci(dir):
	sciL = []
	for root, dirs, files in os.walk(dir):
		for file in files:
			if file[-4:len(file)].lower() == '.sci':
				sci = os.path.join(root, file)
				sciL.append(sci)
	return sciL

if __name__ == '__main__':
	if len(sys.argv)==5:
		wkspc = sys.argv[1] # 工作空间路径
		map = sys.argv[2]  # 地图名称
		dir = sys.argv[3] # 缓存生成目录
		time_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		if os.path.isdir(sys.argv[4]):
			scidir = sys.argv[4]
			sciL = findsci(scidir)
			parallel(wkspc, map, dir, sciL)
		time_e = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		print time_s, time_e

