from pprint import pformat
import cgi
import os

def application(environ, start_response):
 #show environment
    output = ['<pre>']
 #html:
    html1 = open("/var/www/reposaurus/static/repopage1.html", "rb")
    contents1 = html1.read()
    output.append(contents1)

 #pick a file:
    if environ['REQUEST_METHOD'] == 'POST':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        output.append("Choose a file from the list below:")
        output.append('<form method="post">')
        output.append('<input type="text" name="filename" placeholder="file name">')
        output.append('<input type="submit"><p>')
    else:
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        output.append("Choose a file from the list below:")
        output.append('<form method="post">')
        output.append('<input type="text" name="filename" placeholder="file name">')
        output.append('<input type="submit"><p>')


 #show files:
    fileList = os.listdir("/var/www/reposaurus/wsgifiles/datasaur/")
    for file in fileList:
        output.append(file)
        output.append("<p>")


    if form['filename'].value in fileList:
        File = open("/var/www/reposaurus/wsgifiles/datasaur/"+form['filename'].value, "rt")
        Filecontents = File.read()
        output.insert(2, "You're viewing: ")
        output.insert(3, form['filename'].value)
        output.insert(4, "<p><span style='font-size:16px; line-height:22px'>")
        output.insert(5, Filecontents)
        output.insert(6, "</span><p>")
    else:
        output.insert(2, "I'm sorry; we don't have that file.  Please choose another.<p>")
 # end html:
    html3 = open("/var/www/reposaurus/static/repopage3.html", "rb")
    contents3 = html3.read()
    output.append(contents3)

 # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output

