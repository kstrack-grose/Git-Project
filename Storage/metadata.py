#!/usr/bin/python

def attempt(file):
	timestamp = "timestamp goes here"
	myFile = open(file, "at")
	myFile.write("#", timestamp)
	myFile.close
	return timestamp


def readLastLine(file):
	myFile = open(file, "rt")
	lines = myFile.readlines()
	lastline = lines[-1]
	print lastline
	return lastline

readLastLine("ostry.py")
