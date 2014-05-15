#!/usr/bin/python

# Roi and Scott and Mr. Chernoh! May 13 2014
# Another valiant but possibly vain attempt at comparing
# And then making new directories

import os, sys, makeFiles, distutils.core

# variables!:

# the user-given path, aka the source of the data we're going to copy
source = raw_input("gimme a path ")

# list of contents of said directory
srcCont = os.listdir(source)

# the current working directory, aka destination where we'll
# make a new directory with the user's data
# this is a proxy for our repo
repo = str(os.getcwd())

# list of contents in current working directory (repo)
repoCont = os.listdir(repo)

# this will be the new directory made in the repo
# where we will put the user's data
destination = repo+'/'+raw_input('name new version: ')

# This function should go through the contents of every file in the 
# working directory (i.e. repo) and the directory/file modified or given
# by the user
# and then, if they're different from each other, make a new directory
# in the repo
# and move the contents of the user's directory into the new directory
# this is an early version of versioning
# eventually we will number each new directory sequentially
# for now it's just raw input
def compareAndMakeDirectories(userPath, newVersion, repoDirectoryContents, userDirectoryContents):
# think of the paramaters this way for now:
# source = userPath
# destination = newVersion
# repoCont = repoDirectoryContents
# srcCont = userDirectoryContents
	
	repoContentList = []
	userContentList = []

# go through contents of old directory	
	for x in range(0, len(repoDirectoryContents)):
        	file = str(repoDirectoryContents[x])
        	repoContents = makeFiles.readFiles(file)
		repoContentList.append(repoContents)

# go through contents of user-given directory
	for x in range(0, len(userDirectoryContents)):
                # the reason we're putting userPath in here is so that
		# the program will have the path to the file
		file = userPath+'/'+str(userDirectoryContents[x])
                userContents = makeFiles.readFiles(file)
		userContentList.append(userContents)
	
	
	# if there are no changes then return no changes
 	if repoContentList == userContentList:
		print "no change"
		return  
		
	
	elif userContentList != repoContentList:
		distutils.dir_util.copy_tree(userPath, newVersion)
		return

	else:
		print "something went wrong"
		return	

compareAndMakeDirectories(source, destination, repoCont, srcCont)
