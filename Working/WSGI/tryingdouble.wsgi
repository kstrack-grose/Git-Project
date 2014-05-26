from pprint import pformat
import cgi
import os
import sys

"""
def application(environ, start_response):
    # show the environment:
    output = ['<pre>']
    output.append(pformat(environ))
    output.append('</pre>')

    if environ['REQUEST_METHOD'] == 'POST':
        # show form data as received by POST:
	form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        output.append('<h1>FORM DATA</h1>')
        output.append(form['test'].value)
        #output.append(form['test2'].value)
        if (form['test'].value != ""):
            output.append("<p>Things in quotes")
	#elif (form['test'].value == ""):
	    #output.append("<p>Put something in there please, no joke")
        #if (form['test2'].value != ""):
            #output.append("<p>Success")		
	#elif (form['test2'].value == False):
            #output.append("<p>done fucked up")


#output.append("<p>CHECK THE FILE YOU PEOPLE!")
#myFile = open("wsgitest.txt", "at")
#myFile.write(form['test'].value.write(wsgitest.txt))
#myFile.close
    else:
	#create a simple form if no input has been posted to us
        output.append('<form method="post">')
        output.append('<input type="text" name="test">')
        #output.append('<input type="submit">')
        #output.append('</form>')
        #output.append('<form method="post">')
        output.append('<input type="text" name="test2">')
        output.append('<input type="submit">')
        output.append('</form>')
    
    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    #def writeContents():
        #newFile=open(newFileName, "wt")
        #newFile.write(
    return output
"""
def application(environ, start_response):
    # show the environment:
    output = ['<pre>']
    output.append(pformat(environ))
    output.append('</pre>')

    if environ['REQUEST_METHOD'] == 'POST':
        # show form data as received by POST:
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        output.append('<h1>FORM DATA</h1>')
        output.append(form['test'].value)
        #output.append(form['test2'].value)
        if (form['test'].value != ""):
            output.append("<p>Things in quotes")
        #elif (form['test'].value == ""):
            #output.append("<p>Put something in there please, no joke")
        #if (form['test2'].value != ""):
            #output.append("<p>Success")
        #elif (form['test2'].value == False):
            #output.append("<p>done fucked up")


#output.append("<p>CHECK THE FILE YOU PEOPLE!")
#myFile = open("wsgitest.txt", "at")
#myFile.write(form['test'].value.write(wsgitest.txt))
#myFile.close
    else:
        #create a simple form if no input has been posted to us
        output.append('<form method="post">')
        output.append('<input type="text" name="test">')
        #output.append('<input type="submit">')
        #output.append('</form>')
        #output.append('<form method="post">')
        output.append('<input type="text" name="test2">')
        output.append('<input type="submit">')
        output.append('</form>')

    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    #def writeContents():
        #newFile=open(newFileName, "wt")
        #newFile.write(
    return output

