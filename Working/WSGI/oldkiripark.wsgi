from pprint import pformat
import cgi

def application(environ, start_response):
    # show the environment:
    output = ['<pre>']

    if environ['REQUEST_METHOD'] == 'POST':
        # show form data as received by POST:
	form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        output.append('<h1>FORM DATA</h1>')
        output.append(form['test'].value)
	output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
        output.append('<input type="file" name="test">')
        output.append('<input type="submit">')
        output.append('</form>')
	output.append("<p>HAPPINESS")
	# append the form data to the file
   	output.append('<p>attempting to write to file')
#        var = str(form['test'].value)
    	myFile = open("/var/www/wsgifiles/dinoeggs/dino-egg", "wb")
    	myFile.write("\n")
    	myFile.write(form['test'].value)
    	myFile.close()
    	output.append('<p>maybe I wrote to that file')

    else:
	#create a simple form if no input has been posted to us
        output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
        output.append('<input type="file" name="test">')
        output.append('<input type="submit">')
        output.append('</form>')


    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
