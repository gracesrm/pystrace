'''
get distance among strings of self
usage: python getSelfDistance.py stand/ c
stand/: the sub folder of the str files
c: the cth line of the str file as the reference [0-9)
output disdir/stand/test-case.dis (contains str for 10 tests)
'''
import sys
import os
import editdistance
import numpy as np
import pickle

def Start(subdir, c):
	str_list = "/home/ruimin/pystrace/strdir/" + subdir + "/"

	for root, dirs, strfiles in os.walk(str_list):
		for strfile in strfiles:
			if strfile[-4:] == ".str":
				with open(os.path.join(root,strfile), 'r') as str_fd:
					lines = str_fd.readlines()
					ref = lines[int(c)]
					res = list()
					for line in lines:
						dis = editdistance.eval(ref,line)
						res.append(dis)			
					mean = np.mean(res)
					std = np.std(res)
					dest_file = "/home/ruimin/pystrace/disdir/" + subdir + "/" + strfile[:-4] + ".dis"	
#					os.system("echo " + res_str + " >> " + dest_file)
					with open(dest_file,'ab') as f:
						pickle.dump(res,f)
						line1 = "MEAN:" + str(mean) + "\n"
						line2 = "STD:" + str(std) + "\n"
						f.write(line1)
						f.write(line2)
			


#
# Entry point to the application
#
if __name__ == '__main__':
	Start(sys.argv[1], sys.argv[2])
