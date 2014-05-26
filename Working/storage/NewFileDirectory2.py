#!/usr/bin/python

# Roi and Chernoh and Scott and Xander and Kiri (and Andrew) May 12, 2014
# This program makes a new directory based on compared changes
#import shutil
#import os
#source = os.listdir("/tmp/")
#destination = "/tmp/newfolder/"
#for files in source:
    #if files.endswith(".txt"):
        #shutil.copy(files,destination)

#import shutil  
#shutil.copyfile('/path/to/file', '/path/to/other/phile')  

import os, sys, makeFiles

path = str(os.getcwd())

dirs = os.listdir(path)

newPath = "/home/rkarlinsky/GitHub/Git-Project/storeTest/storage"

newDirs = os.listdir(newPath)

for x in range(0, len(dirs)):
	file = str(dirs[x])
	file2 = str(newDirs[x])
	if file == file2:
		print file
		print "no change"
	if file != file2:
		makeFiles.makeDir(version1)
		print "new directory made"



