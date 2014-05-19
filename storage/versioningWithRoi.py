#!/usr/bin/python

# Roi and Scott and Mr. Chernoh! May 15 2014
# This will use Kiri's metadata.timeStamp and metadata.readLastLine function to 
# append timestamps to a settings file that will live in the repo directory.
# We can then keep track of which directory has the most up to date versions
# of the user's files, and to name new directories iteratively, with a 
# timestamp to boot!

import os

# A Function that creates A list Of the directories (versions) within the users
# repo directory. It will return the last directory name in the list.

# Repo will be the path for the users repo, in which the individual version
# directories will live.

def lastDir(repo):
	# because oslist.dir lists contents in an arbitrary order, sorted()
	# sorts the list numerically
        repoList = sorted(os.listdir(repo))
      	print repoList
	# lastDir will become the last entry in repoList
	lastDir = repoList[-1]
	print lastDir
        return lastDir

# Raw input for now, a real path for later.
lastDir(raw_input("Give me a directory full of directories to list "))




# This will eventually be the timestamp, I just copied it from the metadata.py
# file. Basically just saving it for laterz.

def timeStamp(file):
        import datetime
        timestamp = str(datetime.datetime.now())
        myFile = open(file, "at")
        myFile.write("#")
        myFile.write(timestamp)
        myFile.close
        return timestamp


def readLastLine(file):
        myFile = open(file, "rt")
        lines = myFile.readlines()
        lastline = lines[-1]
        print lastline
        myFile.close
        return lastline


