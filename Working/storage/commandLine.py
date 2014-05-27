#!/usr/bin/python

import shutil

        # takes file to move, and puts it in dinoeggs directory
def dinoPush(file, destination):
        shutil.copy(file, "/var/www/wsgifiles/dinoeggs")


dinoPush(raw_input("Gimme the path of the file you want to upload "), "/var/www/wsgifiles/dinoeggs")
