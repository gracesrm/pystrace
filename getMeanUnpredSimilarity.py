import os, sys, glob
import numpy as np
import matplotlib.pyplot as plt

def writeToCSV():
    for i in range(5):
        cmd = "cat ratiodir/0_" + str(i) + "/* > ratiodir/similarity_M" + str(i) + ".csv"
        os.system(cmd)
    for i in range(18):
        i += 1
        if i == 15:    continue
        idx = i if i<16 else i-1
        cmd = "cat ratiodir/" + str(i) + "_0/* > ratiodir/similarity_U" + str(idx) + ".csv" 
        os.system(cmd)
#    cmd = "cat ratiodir/stand/* > ratiodir/similarity_St.csv"
#    os.system(cmd)

def getMean():
    width = 0.9
    files = glob.glob("ratiodir/similarity_*")
    label_list, mean_list = list(), list()
    for i in range(5):
        _file = "ratiodir/similarity_M" + str(i) + ".csv"
        arr = np.loadtxt(_file, delimiter=',', usecols=(0,))
        _mean = np.nanmean(arr)
        label_list.append(_file.split('/')[-1].split('_')[1].split('.')[0])
        mean_list.append(_mean)
    for i in range(17):
        i += 1
        _file = "ratiodir/similarity_U" + str(i) + ".csv"
        arr = np.loadtxt(_file, delimiter=',', usecols=(0,))
        _mean = np.nanmean(arr)
        label_list.append(_file.split('/')[-1].split('_')[1].split('.')[0])
        mean_list.append(_mean)
    fig = plt.figure(figsize=(18, 6), dpi=240)
    ind = np.arange(len(files)) * 1.2
    plt.bar(ind, mean_list, width, color='blue')
    plt.xticks([r*1.2 for r in range(len(files))], label_list, rotation=90)
    fig.savefig("similarity.png")
    plt.close()

if __name__ == "__main__":
    writeToCSV()
    getMean() 
