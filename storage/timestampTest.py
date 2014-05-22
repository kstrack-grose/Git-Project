#!/usr/bin/python

# may 22, 2014
# an attempt to make a clean timestamp

import time, datetime

ts = time.time() 
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%x.%X')
print timestamp

