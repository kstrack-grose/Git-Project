#!/usr/bin/python
##################### CHERNOH #################
# still trying to copy contents of a directory
# and create new version of the directory if contents are modified

import os 
import shutil
import stat

dst = raw_input("version name: ")
TestDirFiles = '/Intro-S2014/students/cjalloh/TestDirFiles'  #this path is only for my own local directory

def trackNversion(TestDirFiles, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for contents in os.listdir(TestDirFiles):
        s = os.path.join(TestDirFiles, contents)
        d = os.path.join(dst, contents)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(TestDirFiles).st_mtime - os.stat(dst).st_mtime > 1:
                shutil.copy2(s, d)
	

trackNversion(TestDirFiles, dst, symlinks=False, ignore=None)
