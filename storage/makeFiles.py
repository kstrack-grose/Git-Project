#!/usr/bin/python
import os
#comparing files and, if different, making a new one

def compareAndMake(file, oldFile, newFileName):
#parameters: 
#the name of the file that's been commited
#the name of the old version of the file
#the name you want to give that file
	myFile = open(file, "rt")
	contents = myFile.read()
	oldfile = open(oldFile, "rt")
	oldContents = oldfile.read()

	if contents == oldContents:
	# things are the same; don't create a new file
		print "no change"
		myFile.close
		oldfile.close
		return

	elif contents != oldContents:
	# create a new file
		newFile = open(newFileName, "wt")
		newFile.write(contents)
		print "new file made"
		myFile.close
		oldfile.close
		newFile.close
		return

	else:
	# a catch-all
		"what's going on????"
		myFile.close
		oldfile.close
		return


#make a new directory
dirName = ""
path = "/home/kstrack-grose/Git-Project/Git-Project/storage/%s" % dirName
os.makedirs(path)
