#!/usr/bin/python

# Roi and Chernoh and Scott and Xander and Kiri (and Andrew) May 12, 2014
# This program makes a new directory based on compared changes

import os, sys, shutil

# this is the directory the user is using
# this is the current working directory
pathIn = str(os.getcwd())

newDirName = pathIn+'/'+raw_input("gimme path ")

# this grabs the contents from the user's directory

contentsFrom = os.listdir(pathIn)

for files in contentsFrom:
	shutil.copy(str(files), str(newDirName))
	print "new directory made!"

os.makedirs(newDirName, 0777) 
