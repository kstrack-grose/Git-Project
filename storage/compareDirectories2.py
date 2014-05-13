#!/usr/bin/python

# Roi and Scott and Mr. Chernoh! May 13 2014
# Another valiant but possibly vain attempt at comparing
# And then making new directories

import os, sys, makeFiles, shutil

# initialize variables
path = str(os.getcwd())

# list of all the fiels in a directory
dirs = os.listdir(path)

#for loop that calls on compareAndMake, which compares files
#and makes new ones if they are different
#parameters: new file name, old file name, 
#and what you want the new file to be named
#we're going to remove the last parameter.
for x in range(0, len(dirs)):
        file = str(dirs[x])
        print file
        makeFiles.readFiles(file)
	
