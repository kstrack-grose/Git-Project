#!/usr/bin/python

	# import main modules
import urllib
import urllib2
#data for upload
data = 
#talk to a url
request = urllib2.Request('http://www.reposaurus.org')
print 'Request method before data:', request.get_method()
#encode and bundle data
request.add_data(urllib.urlencode(data))
print 'Request method after data :', request.get_method()
#send data with a header
request.add_header('User-agent', 'PyMOTW (http://www.reposaurus.org)')

print
print 'OUTGOING DATA:'
print request.get_data()
#get response back
print
print 'SERVER RESPONSE:'
print urllib2.urlopen(request).read()
