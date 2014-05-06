#!/usr/bin/python

def attempt(file):
	timestamp = "timestamp goes here"
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

attempt("ostry.py")
readLastLine("ostry.py")
