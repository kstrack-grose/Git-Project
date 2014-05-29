#!/usr/bin/python

#imports
import time
import datetime
from datetime import datetime
from datetime import timedelta

#list to place break times in
times = []

#start/end
start = datetime(2014, 4, 1, 2, 00)
end = datetime(2014, 4, 1, 8, 30)

#just to check in, visually
print "start at", start
print "end at", end

#create caches of time, I guess
totalTime = end - start
totalMin = totalTime.total_seconds()/60
totalHours = totalMin/60 
intHours = int(totalHours//1)

#again, checking in
print "total time is", totalTime
print "total minutes:", totalMin
print "total hours:", totalHours
print "inthours:", intHours

time = start
print "time:", time



#iterate through in chunks?
print range(0, intHours)
print "\n\n\n"

for x in range(0, intHours):
	time = time + timedelta(minutes = 55)
	times.append(["Start of break is", time.strftime('%d, %r')])
	time = time + timedelta(minutes = 5)
	times.append(["End of break is", time.strftime('%d, %r')])
	times.append("")

x = len(times)


for y in range(0, x):
	print times[y]






'''
#below works, sort of: ends up in awkward, not nice format

print "\n\n\n"

#iterate!
time = start
while time < (end - timedelta(hours = 1)):
	time += timedelta(0, 0, 0, 0, 55)
	times.append([time, "rehearse"])
	time += timedelta(0, 0, 0, 0, 5)
	times.append([time, "break"])

print times
'''

'''
#next: find out how to do a mealbreak
halfway = (end - start)/2 + start
print "halfway", halfway
startmeal = halfway - timedelta(0, 0, 0, 0, 30)
endmeal = halfway + timedelta(0, 0, 0, 0, 30)
print "Your meal will be:", startmeal, "-", endmeal



third = (end - start)/3 + start
startmeal1 = third - timedelta(0, 0, 0, 0, 30)
endmeal1 = third + timedelta(0, 0, 0, 0, 30)

secondThird = (2*(end-start))/3 + start
startmeal2 = third - timedelta(0, 0, 0, 0, 30)
endmeal2 = third + timedelta(0, 0, 0, 0, 30)

print "Your first meal will be:", startmeal1, "-", endmeal1, "\b."
print "Your second meal will be:", startmeal2, "-", endmeal2, "\b."
'''












'''
#next task; to iterate through a while loop
#and my real challenge is to save a bunch of times
#as beginning and ends of breaks
#so
#help?
#re: iterating through changing variables
#variables
time = start
run = timedelta(0, 0, 0, 0, 55)
breakk = timedelta(0, 0, 0, 0, 5)

#again to check it out
print "run", run
print "break", breakk

while time < end:
    startbreak1 = time + run
    print "startbreak1", startbreak1
    endbreak1 = startbreak1 + breakk
    print "endbreak1", endbreak1
    time = endbreak1
#and then iterate through, saving things as startbreak2 and endbreak2 and such on.  how?
#is that even possible?
#it should be
#because I'm sure it's useful to people besides me
'''
