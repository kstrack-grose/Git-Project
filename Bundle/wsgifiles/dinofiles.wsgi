from pprint import pformat
import cgi
import os

def application(environ, start_response):
 #show environment
    output = ['<pre>']
 #html:
    html1 = open("/var/www/static/repopage1.html", "rb")
    contents1 = html1.read()
    output.append(contents1)
 #pick a file:
    output.append("Choose a file from the list below:")
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    output.append('<form id="upload" name="upload" method="POST">')
    output.append('<input type="text" name="filename" placeholder="file name">')
    output.append('<form method="post">')
    output.append('<input type="submit"><p>')

 #show files:
    fileList = os.listdir("/var/www/wsgifiles/datasaur/")
    for file in fileList:
        output.append(file)
        output.append("<p>")
#    output.append(form['upload'].value)
#    if form['filename'].value in fileList:
#        File = open("/var/www/wsgifiles/datasaur/"+form['filename'].value, "rt")
#        Filecontents = File.read()
#        output.append(Filecontents)

 # end html:
    html3 = open("/var/www/static/repopage3.html", "rb")
    contents3 = html3.read()
    output.append(contents3)

 # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output

