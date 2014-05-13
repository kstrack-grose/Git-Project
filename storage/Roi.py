#!/usr/bin/python

# Roi and Chernoh and Scott and Xander and Kiri (and Andrew) May 12, 2014
# This program makes a new directory based on compared changes

import os, sys, shutil, makeFiles

# this is the current working directory
pathIn = str(os.getcwd())

# this is the directory the user is using
newDirName = raw_input("name of directory ")


shutil.move(newDirName, pathIn)
 
