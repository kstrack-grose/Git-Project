#!/usr/bin/python

	# Kiri and Xander and Roi... and Mr. Chernor(this is the correct spelling)!
	# May 18, 2014

	# This is the working program of comparing the last updated version
	# in a repo and making a new directory with user-given data
	# if changes had been detected 

	#Run this program in root. If you are having weird permission errors, this is why.

import os, sys, makeFiles, distutils.core, datetime, time

########################### FUNCTIONS ################################

######### LastDir!

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
        #print lastDir
        return lastDir


######### compareAndMakeDirectories !


def compareAndMakeDirectories(userPath, newVersion, versionDirectoryContents, userDirectoryContents):
	# think of the paramaters this way for now:
	# source = userPath
	# destination = newVersion
	# recentVersionCont = versionDirectoryContents
	# sourceFiles = userDirectoryContents

        versionContentList = []
        userContentList = []

# go through contents of old directory  
        for x in range(0, len(versionDirectoryContents)):
                file = recentVersion+'/'+ str(versionDirectoryContents[x])
                versionContents = makeFiles.readFiles(file)
                versionContentList.append(versionContents)

# go through contents of user-given directory
        for x in range(0, len(userDirectoryContents)):
                # the reason we're putting userPath in here is so that
                # the program will have the path to the file
                file = userPath+'/'+str(userDirectoryContents[x])
                userContents = makeFiles.readFiles(file)
                userContentList.append(userContents)

#Ignore this, it is there incase we need to do more troubleshooting
#	print "userContentList"
#	print userContentList
#	print "sorted user"
#	print sorted(userContentList)

#	print "versionContentList"
#	print versionContentList
#	print "sorted version"
#	print sorted(versionContentList)


# if there are no changes then return no changes
        if sorted(versionContentList) == sorted(userContentList):
                print "no change"
		for fileName in userDirectoryContents:
 			os.remove(userPath+"/"+fileName)
                return

# newVersion will eventually come from repo (being the path for the
# user's repo) + '.' + timeStamp (so that it will be named so that it 
# is after lastDir, and becomes the NEW most recent directory, or 
# lastDir the NEXT time you run this function.
        elif sorted(userContentList) != sorted(versionContentList):
                distutils.dir_util.copy_tree(userPath, newVersion)
                for fileName in userDirectoryContents:
                	os.remove(userPath+"/"+fileName)
		return

        else:
                print "something went wrong"
                return

################################################################################


############################### VARIABLES ######################################

	# the user-given path, aka the source of the data we're going to copy

source = "/var/www/wsgifiles/dinoeggs"

	# list of contents (aka files) of user given path
sourceFiles = os.listdir(source)

	# this is a proxy for the repo
repo = raw_input("gimme a repo path ")

	# This is the user's most recently updated
	# directory
	# we're getting that path with the lastDir function
recentVersion = repo +'/'+str(lastDir(repo))

	# list of contents in most recently updated directory
recentVersionCont = os.listdir(recentVersion)

	# this is a timestamp
	# it'll return the name of the month, the day, the year
	# and the time down to the seconds
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%B-%d-%y.%H.%M.%S')

	# This will be the new home of the latest version given by the user 
destination = repo+'/'+timestamp


	# Now we're calling the program! Magic presto!
compareAndMakeDirectories(source, destination, recentVersionCont, sourceFiles)

