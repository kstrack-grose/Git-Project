#!/usr/bin/python

def attempt(file):
	timestamp = "timestamp goes here"
	myFile = open(file, "at")
	myFile.write(timestamp)
	myFile.close
	return timestamp


#make a function that will take the last line of the file and read it back
