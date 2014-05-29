from pprint import pformat
import cgi

def application(environ, start_response):
 # show the environment:
    output = ['<pre>']

 # first half of hmtl contents
    html1file = open("/var/www/static/index1.html", "rb")
    html1contents = html1file.read()
    output.append(html1contents)

 # variable for field storage
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
 # username and password forms
    output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
    output.append('<div id="fileupload">Choose a file: ')
    output.append('<p><input type="file" name="file"')
    output.append(' placeholder="file"><br></div>')
    output.append('<div id = "fileupload"> <input type="submit"></div>')
    output.append('</form>')
    output.append('</div><!--loginend-->')
 # if stuff has been POSTed
    if environ['REQUEST_METHOD'] == 'POST':
     # show form data as received by POST:
        file = form['file'].value
        myFile = open("/var/www/wsgifiles/datasaur/"+form['file'].filename, "wt")
        myFile.write(file)
        myFile.close()
        output.append('<div id="uploadedfile">')
        output.append("<span font-size: '24px'> Upload was successful: ")
        output.append(form['file'].filename)
        output.append('</span>')
        output.append('<p><p><p>')
        output.append(file)        
        output.append('</div>')

 #second half of html file
    html2file = open("/var/www/static/index2.html", "rb")
    html2contents = html2file.read()
    output.append(html2contents)

    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
