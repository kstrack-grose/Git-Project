from pprint import pformat
import cgi

def application(environ, start_response):
 # usernames and passwords
    userDict = {
"Arthur":"d10i",
"Ayesha":"e11m",
"Carlos":"j7g",
"Chernoh":"l3e",
"Chris":"g4k",
"Jeffrey":"i9d",
"Jenna":"h8b",
"Kiri":"b2f",
"Megan":"m12l",
"Robin":"k1h",
"Roi":"c5c",
"Scott":"a3j",
"Xander":"f6a",
}
 # start the output fom
    output = ['<pre>']
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
 # open the first half of the html file (before username and password)
    index1 = open("/var/www/static/index1.html","rb")
    html1contents = index1.read()
    output.append(html1contents)
 # add username and password forms
#    output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
    output.append('<input type="text" name="username">')
    output.append('<form method="post">')
    output.append('<input type="text" name="password">')
    output.append('<input type="submit">')
    output.append('</form>')
 # if posted:
    if environ['REQUEST_METHOD'] == 'POST':
        output.append("posted things")
        if (form['username'].value != ""):
            output.append("username exists")
        if (form['password'].value != ""):
            output.append("password exists")
      # if username is correct:
      # print them out (just for now!)
#        output.append(form['username'].value
#        output.append(form['password'].value
      # compare input to the values in username dictionary
#        if form['username'].value in userDict:
      # if it's in the dictionary, compare inputted password to the password in dictionary
#            if form['password'].value == userDict[form['username'].value]:
#                output.append("<p>GREAT SUCCESS")

 # second half of html file
    index2 = open("/var/www/static/index2.html", "rb")
    html2contents = index2.read()
    output.append(html2contents)

    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
