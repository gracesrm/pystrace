#!/bin/bash
# Usage: source start_strace2csv.sh root_dir_tr

find $1 -name "*.tr" > trace_src_list
while read trace_src
do 
	trace_dest=$(echo $trace_src | cut -d '.' -f1)
	trace_dest=$trace_dest'.csv'
#	echo $trace_src
#	echo $trace_dest
	python strace2csv.py -o $trace_dest $trace_src #$trace_src
	sleep 0.1

done<trace_src_list

rm trace_src_list
