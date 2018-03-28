'''
get distance among strings of self
usage: python getDistanceFromStand.py stand_dir unpred_dir c
stand_dir/: the sub folder of the str files (standard)
unpre_dir/: ditto but unpred
c: the cth line of the str file as the reference [0-9)
output e.g. disdir/0_0/test-case.dis (contains str for 10 tests)
'''
import sys
import os
import editdistance
import numpy as np
import pickle

def Start(stand_dir, unpred_dir, c):
	subdir = unpred_dir.split('/')[-2]
	print subdir
	for rt, drs, strfs in os.walk(unpred_dir):
		for strf_unp in strfs:
			if strf_unp[-4:] == ".str":
				print strf_unp
				strf_std = stand_dir + strf_unp[:-6] + ".str"
				print strf_std
				with open(strf_std,'r') as str_fd, open(os.path.join(rt,strf_unp), 'r') as str_unp_fd:
					ref = str_fd.readlines()[int(c)]
					comp = str_unp_fd.readline()
					dis = editdistance.eval(ref, comp)
					dest_file = "/home/ruimin/pystrace/disdir/" + subdir + "/" + strf_unp[:-4] + ".dis"	
					with open(dest_file,'ab') as f:
						f.write(str(dis) + '\n')


#
# Entry point to the application
#
if __name__ == '__main__':
	Start(sys.argv[1], sys.argv[2], sys.argv[3])
