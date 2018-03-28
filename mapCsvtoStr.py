'''
map csv file to str
usage: python mapCsvtoStr.py full_path
output strdir/stand/test-case.str (contains str for 10 tests)
'''
import sys
import os
import glob
import csv


def Start(csv_list):
	syscall_map = {"arch_prctl":'a',\
			"pipe":'b',\
			"fcntl":'c',\
			"ioctl":'d',\
			"write":'e',\
			"mmap":'f',\
			"getrlimit":'g',\
			"rt_sigprocmask":'h',\
			"open":'i',\
			"YSCAL":'j',\
			"getdents":'k',\
			"set_tid_address":'l',\
			"rt_sigaction":'m',\
			"setrlimit":'n',\
			"SIGCHLD":'o',\
			"execve":'p',\
			"wait4":'q',\
			"munmap":'r',\
			"close":'s',\
			"set_robust_list":'t',\
			"chdir":'u',\
			"brk":'v',\
			"futex":'w',\
			"KILL":'x',\
			"rt_sigreturn":'y',\
			"mprotect":'z',\
			"openat":'A',\
			"read":'B',\
			"getcwd":'C',\
			"exit_group":'D',\
			"SIGSEGV":'E',\
			"fstat":'F',\
			"stat":'G',\
			"vfork":'H',\
			"access":'I',\
			"writev":'J',\
			"lseek":'K',\
			"madvise":'L',\
			"mremap":'M'}

	'''
	YSCAL is SYSCALL, truncated because no "" in the log
	'''
	for root, dirs, csvfiles in os.walk(csv_list):
		for csvfile in csvfiles:
			if csvfile[-4:] == ".csv":
				res_str = ""
				src_file = os.path.join(root, csvfile)
				#print src_file
				with open(src_file, 'r') as csv_fd:
					for line in csv_fd.readlines():
						syscall = line.strip().split(',')[1]
						res_str += syscall_map[syscall[1:-1]]  #remove the ""
					subdir = src_file.split('/')[-2] + '/'
					dest_file = "/home/ruimin/pystrace/strdir/" + subdir + csvfile[:-4] + ".str"
					#print dest_file	
					with open(dest_file,'a+') as f:
						f.write(res_str + '\n')
			


#
# Entry point to the application
#
if __name__ == '__main__':
	Start(sys.argv[1])
