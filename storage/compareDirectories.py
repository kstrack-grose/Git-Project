#!/usr/bin/python

import os, sys, makeFiles

#initalize variables
path = str(os.getcwd())

#list of all the files in a directory
dirs = os.listdir(path)

#for loop that calls on compareAndMake, which compares files
#and makes new ones if they are different
#parameters: new file name, old file name, 
#and what you want the new file to be named
#we're going to remove the last parameter.
for x in range(0, len(dirs)):
	file = str(dirs[x])
	print file
	makeFiles.compareAndMake(file, file, file)


