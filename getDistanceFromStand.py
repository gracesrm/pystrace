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
	for rt, drs, strfs in os.walk(unpred_dir):
		for strf_unp in strfs:

			unpred_src = os.path.join(rt, strf_unp)
			subdir = unpred_src.split('/')[-2] + '/'
			# print subdir    #  0_0/  stand/
			if "stand" in subdir:
				continue

			if strf_unp[-4:] == ".str":
				# print unpred_src   # strdir/0_0/xxx_0.str
				strf_std = stand_dir + strf_unp[:-6] + ".str"
				# print strf_std   # strdir/stand/xxx.str

				with open(strf_std,'r') as str_fd, open(unpred_src, 'r') as str_unp_fd:
					ref = str_fd.readlines()[int(c)]
					comp = str_unp_fd.readline()
					try:
						dis = editdistance.eval(ref, comp)
						ratio = 1- dis/float(max(len(ref), len(comp)))
						# print str(ratio)
					except:
						pass
					dest_file = "/home/ruimin/pystrace/disdir/" + subdir + strf_unp[:-6] + ".dis"
					dest_file_rt = "/home/ruimin/pystrace/ratiodir/" + subdir + strf_unp[:-6] + ".rt"
					# print dest_file
					with open(dest_file_rt,'ab') as f:
						f.write(str(ratio) + '\n')


#
# Entry point to the application
#
if __name__ == '__main__':
	Start(sys.argv[1], sys.argv[2], sys.argv[3])
