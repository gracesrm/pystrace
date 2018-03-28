import sys
import os
import glob
import csv


def Start():
	csv_list = "/home/ruimin/pystrace/csvdir/" # recursive=Tru
	syscall_dict = dict()

	for root, dirs, csvfiles in os.walk(csv_list):
		# print str(len(csvfiles))
		for csvfile in csvfiles:
			if csvfile[-4:] == ".csv":
				# print csvfile
				with open(os.path.join(root,csvfile), 'r') as csv_fd:
					for line in csv_fd.readlines():
						syscall = line.strip().split(',')[1]
						print syscall[1:-1]
						if not bool(syscall_dict.get(syscall)):
							syscall_dict[syscall] = 1
						else:
							syscall_dict[syscall] += 1

	with open('syscall_freq.csv','wb') as f:
		writer =csv.writer(f)
		for key, value in syscall_dict.items():
			writer.writerow([key,value])
			
	print "syscall set length is " + str(len(syscall_dict))
	print 'finished'


#
# Entry point to the application
#
if __name__ == '__main__':
	Start()
