#!/usr/bin/python

# Roi and Chernoh and Scott and Xander and Kiri (and Andrew) May 12, 2014
# This program makes a new directory with user given data
# It works too!!

import os, sys, distutils.core

# this is the current working directory
path = str(os.getcwd())

# this makes a new directory in the current working directory 
# with a raw input name
# the idea is to have a location within the repo to put data
# the user has inputed 
destination = path+'/'+raw_input('give a place to go: ')

# this is where we're copying from
# so the website will give us a path with user-inputed info
# and then we'll copy those contents
source = "/home/rkarlinsky/GitHub/Git-Project/New" 

# distutils lets you copy a tree and put it into
# a new directory, without deleting the old one
# which is what shutil did
# we don't like shutil (Robin)
# so this copies user data into a new directory
distutils.dir_util.copy_tree(source, destination)
