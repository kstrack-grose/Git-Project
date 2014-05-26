from pprint import pformat
import cgi 

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
        if form['test'].value == "dogs":
		output.append("<p>HAPPINESS")
    else:
	#create a simple form if no input has been posted to us
        output.append('<form method="post">')
        output.append('<input type="text" name="test">')
        output.append('<input type="submit">')
        output.append('</form>')

    output.append('attempting to write to file')
    myFile = open("/home/kstrack-grose/FILE.txt", "at")
    myFile.write("gah")
    myFile.close()

    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
