#!/usr/bin/python

# Roi and Scott and Mr. Chernoh! May 13 2014
# Another valiant but possibly vain attempt at comparing
# And then making new directories

import os, sys, makeFiles, distutils.core, datetime

# variables!:

# the user-given path, aka the source of the data we're going to copy
source = raw_input("gimme a source path ")

# list of contents of said directory
sourceCont = os.listdir(source)

# this is a proxy for the repo
repo = raw_input("gimme a repo path ")


# A Function that creates A list Of the directories (versions) within the 
# user's repo directory. It will return the last directory name in the list.

# Repo will be the path for the users repo, in which the individual version
# directories will live.

def lastDir(repo):
        # because oslist.dir lists contents in an arbitrary order, sorted()
        # sorts the list numerically
        repoList = sorted(os.listdir(repo))
        # lastDir will become the last entry in repoList
        lastDir = repoList[-1]
        # print lastDir
        return lastDir


# This is the user's most recently updated
# directory
# we're getting that path with the lastDir function
recentVersion = repo +'/'+str(lastDir(repo))

# list of contents in most recently updated directory
recentVersionCont = os.listdir(recentVersion)

# this will be the new directory made in the repo
# where we will put the user's data

# This will be the new home of the latest version given by the user
# which will be timestamped 

destination = repo+'/'+str(datetime.datetime.now())

# This function should go through the contents of every file in the 
# working directory (i.e. repo, which will be user specific) and the 
#directory/file modified or given by the user (the tmp file from WSGI)
# and then, if they're different from each other, make a new directory
# in the repo which will be named using the newVersion paramater (more details
# below) and move the contents of the tmp/WSGi directory into the new directory
# for now it's still raw input, to be implemented soon, along with the naming
# for newVersion. If you were looking for something to do, or something...

def compareAndMakeDirectories(userPath, newVersion, versionDirectoryContents, userDirectoryContents):
# think of the paramaters this way for now:
# source = userPath
# destination = newVersion
# recentVersionCont = versionDirectoryContents
# sourceCont = userDirectoryContents
	
	versionContentList = []
	userContentList = []

# go through contents of old directory	
	for x in range(0, len(versionDirectoryContents)):
        	file = str(versionDirectoryContents[x])
        	versionContents = makeFiles.readFiles(file)
		versionContentList.append(versionContents)

# go through contents of user-given directory
	for x in range(0, len(userDirectoryContents)):
                # the reason we're putting userPath in here is so that
		# the program will have the path to the file
		file = userPath+'/'+str(userDirectoryContents[x])
                userContents = makeFiles.readFiles(file)
		userContentList.append(userContents)
	
	
	# if there are no changes then return no changes
 	if versionContentList == userContentList:
		print "no change"
		return  
		
	# newVersion will eventually come from repo (being the path for the
	# user's repo) + '.' + timeStamp (so that it will be named so that it 
	# is after lastDir, and becomes the NEW most recent directory, or 
	# lastDir the NEXT time you run this function.
	elif userContentList != versionContentList:
		distutils.dir_util.copy_tree(userPath, newVersion)
		return

	else:
		print "something went wrong"
		return	

compareAndMakeDirectories(source, destination, recentVersionCont, sourceCont)
