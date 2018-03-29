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

	with open('tmp','r') as fff:
		tmpfiles = fff.readlines()
		for tmpfile in tmpfiles:
			tmpfile = tmpfile.strip('\n')
			unpre_dir = tmpfile.split('/')
			subdir = unpre_dir[-2] + '/'
			strf_std = stand_dir + unpre_dir[-1][:-6] + ".str"
			print strf_std
			print tmpfile
			with open(tmpfile, 'r') as str_unp_fd, open(strf_std,'r') as str_fd:
				ref = str_fd.readlines()[int(c)]
				comp = str_unp_fd.readline()
				try:
					dis = editdistance.eval(ref, comp)
				except:
					pass
				dest_file = "/home/ruimin/pystrace/disdir/" + subdir + unpre_dir[-1][:-6] + ".dis"	
				# print dest_file
				with open(dest_file,'ab') as f:
					f.write(str(dis) + '\n')


#
# Entry point to the application
#
if __name__ == '__main__':
	Start(sys.argv[1], sys.argv[2], sys.argv[3])
