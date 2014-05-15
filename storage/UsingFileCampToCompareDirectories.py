#!/usr/bin/python
# CHERNOH

import filecmp #for comparting both files and directories
filecmp.cmp()
filecmp.dircmp('latestDirectory','newDirectory') #now we want to compare these two directories' contents

# filters and ignores if no change/difference
