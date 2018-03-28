### start_strace2csv.sh ###

.tr file to .csv file (separate strace to syscall name and paras)

### getNumOfTraceType.py ###

python getNumofTraceType.py 

Running coreUtils, we collected 35 types of system calls (syscall_freq.csv)

### mapCsvtoStr.py ###

python mapCsvtoStr.py stand/

Mapping syscalls to chars (.csv to .str), stand/ is the subfolder for csv files, e.g. 0_0/

### getDistance.py ###

Using editdistance to compare different strings, stand/*.dis is compared with self 
