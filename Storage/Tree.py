#!/usr/bin/python

# Roi Ankori-Karlinsky with Xander and Kiri!
# May 2nd, 20134

# The first attempt at coding a tree structure, meaning not a
# real tree structure, but something like it

# Make a Head Directory with an absolute path


import os, sys

#this gives the path name
path = "/home/rkarlinsky/GitHub/Git-Project/Storage/Tree"
# this creates the directory to the path with the mode (u=rwx)
os.mkdir( path, 0755 );

print "Path is created"

# Once we make the head, we need to make sure the program doesn't try to
# make it again, since it won't work
# Next steps would be: write files and other shit to directory
# Kiri's working on that
# Then have functions (or something) that list the directory's
# contents, using the os.listdir(path) method
# then,the program will compare the new contents to the old contents,  
# and if anything changed, it will make a new directory 

# example code:

# the following example shows the usage of listdir() method.

#!/usr/bin/python

# import os, sys

# Open a file
 #path = "/var/www/html/"
 #dirs = os.listdir( path )

# This would print all the files and directories
# for file in dirs:
  #  print file

# if not os.path.exists(directory):
   # os.makedirs(directory)
