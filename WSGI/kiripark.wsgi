from pprint import pformat
import cgi

def application(environ, start_response):
    # show the environment:
    output = ['<pre>']

    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    output.append('<h1>FORM DATA</h1>')
    output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
    output.append('<input type="file" name="test">')
    output.append('<form method="post">')
    output.append('<input type="text" name="test1">')
    output.append('<input type="submit">')
    output.append('</form>')
#    filename = form['test1'].value


    if environ['REQUEST_METHOD'] == 'POST':
        # show form data as received by POST:
	output.append("<p>HAPPINESS")
        output.append(form['test'].value)
	# append the form data to the file
   	output.append('<p>attempting to write to file')
    	output.append('<p>maybe I wrote to that file')
        if (form['test1'].value != ""):
            filename=form['test1'].value
            myFile = open("/var/www/wsgifiles/dinoeggs/"+filename, "wt")
            myFile.write("\n")
            myFile.write(form['test'].value)
            myFile.close()
    else:
	#create a simple form if no input has been posted to us
        output.append("Please submit a file and a filename.")


    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
