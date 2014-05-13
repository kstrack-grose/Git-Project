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
		print "what's going on????"
		myFile.close
		oldfile.close
		return

def makeDir(dirName):
	#make a new directory
	newName = str("/"+dirName)  #this needs to have a / in front 
			#should be softcoded later to reflect versioning
	cwd = str(os.getcwd()) #current working directory
	path = str(cwd+dirName) #concatentate!
	#if os.path.isdir
	os.makedirs(path)  #booyah


def rename(file): #parameter: file to be renamed
	import os
	newName = raw_input("New name: ")
	oldFile = open(file, "rt") #opening old file
	contents = oldFile.read() #saving its innards
	newFile = open(newName, "wt") #opening new file
	newFile.write(contents) #pouring old innards into it
	print "Your file has been renamed."
	#what should happen now is deleting the old file
	os.remove(file)
	oldFile.close
	newFile.close

