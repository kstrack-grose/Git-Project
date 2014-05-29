#!/usr/bin/python

import datetime

timestamp = datetime.datetime.now()

stringtime = timestamp.strftime('%x..%X')

print timestamp
print stringtime
