#!/usr/bin/python

# Roi Ankori-Karlinsky with Xander and Kiri!
# May 2nd, 20134

# The first attempt at coding a tree structure, meaning not a
# real tree structure, but something like it

# Make a Head Directory with an absolute path
# this path is hardcoded though, meaning that nobody else can access this code

import os, sys, ostry

#this gives the path name
path = str(ostry.place)
# this creates the directory to the path with the mode (u=rwx)
if not os.path.exists(path):
	os.makedirs(path, 0755) 

else:
	print "This directory already exists."

print "Path is created"

# Once we make the head, we need to make sure the program doesn't try to
# make it again, since it won't work
# Next steps would be: write files and other shit to directory
# Kiri's working on that
# Then have functions (or something) that list the directory's
# contents, using the os.listdir(path) method
# then,the program will compare the new contents to the old contents,  
# and if anything changed, it will make a new directory 
# 
# example code:

# the following example shows the usage of listdir() method.

# import os, sys
# Open a file
# path = "/home/rkarlinsky/GitHub/Git-Project/Storage/Tree"
# dirs = os.listdir( path )

# This would print all the files and directories
# for file in dirs:
 	#print file

#if not os.path.exists(directory):
	#os.makedirs(directory)

# the Shutil module is great for copying directories into new destinations

#import shutil
#import os
#source = os.listdir("/tmp/")
#destination = "/tmp/newfolder/"
#for files in source:
    #if files.endswith(".txt"):
        #shutil.copy(files,destination)

#import shutil  
#shutil.copyfile('/path/to/file', '/path/to/other/phile')  

#import shutil
#import os
#source = os.listdir("/tmp/")
#destination = "/tmp/newfolder/"
#for files in source:
   # if files.endswith(".txt"):
    #    shutil.move(files,destination)

#import shutil
#import os
#SOURCE = "samples"
#BACKUP = "samples-bak"
# create a backup directory
#shutil.copytree(SOURCE, BACKUP)
#print os.listdir(BACKUP)

# This removes the directory 'three' and anything beneath it in the filesystem.
#import shutil
#shutil.rmtree('one/two/three')
