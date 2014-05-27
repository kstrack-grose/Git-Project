#!/usr/bin/python

import os, sys, getopt, workingCompareDirectories, makeFiles, dinopark

# PseudoCode: here's how I understand this
# We need to write functions for different commands that will
# call the imported programs:
	
	# a command that lists all the commands
	# def dino(argv):
		# print 'Number of arguments:', len(sys.argv), 'arguments.'
		# print 'Argument List:', str(sys.argv)

	# a command that uploads files:
	# def dinoUpload(argv):
		# Does the same as dinopark.wsgi program except without html 
	
		# this is hairy because the dinopark is dependant on
		# html and we need the client to upload stuff
		# directly to the storage

	# a command that updates user's repo:
	# def dinoUpdate(argv):
		# Calls the workingCompareDirectories program


# We got this 	

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
