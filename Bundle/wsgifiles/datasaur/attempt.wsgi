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
    pathDict = {
"Arthur":"/home/kstrack-grose/Git-Project/Arthur/",
"Ayesha":"/home/kstrack-grose/Git-Project/Ayesha/",
"Carlos":"/home/kstrack-grose/Git-Project/Carlos/",
"Chernoh":"/home/kstrack-grose/Git-Project/Chernoh/",
"Chris":"/home/kstrack-grose/Git-Project/Chris/",
"Jeffrey":"/home/kstrack-grose/Git-Project/Jeffrey/",
"Jenna":"/home/kstrack-grose/Git-Project/Jenna/",
"Kiri":"/home/kstrack-grose/Git-Project/Kiri/",
"Megan":"/home/kstrack-grose/Git-Project/Megan/",
"Robin":"/home/kstrack-grose/Git-Project/Robin/",
"Roi":"/home/kstrack-grose/Git-Project/Roi/",
"Scott":"/home/kstrack-grose/Git-Project/Scott/",
"Xander":"/home/kstrack-grose/Git-Project/Xander/",
}

 # start the output form
    output = ['<pre>']
    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
 # open the first half of the html file (before username and password)
    index1 = open("/var/www/static/index1.html","rb")
    html1contents = index1.read()
    output.append(html1contents)
 # add username and password forms

    output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
    output.append('<div id="usrname">Username: <input type="text" name="username" placeholder="Username"><br></div>')

    output.append('<form id="upload" name="upload" method="POST" enctype="multipart/form-data">')
    output.append('<div id="pwd">Password: <input type="text" name="pwd" placeholder="Password"><br></div>')


    output.append('<form method="post">')
    output.append('<p><input type="submit">')
    output.append('</form>')
 # second half of html file
    index2 = open("/var/www/static/index2.html", "rb")
    html2contents = index2.read()
    output.append(html2contents)

 # if posted:
    if environ['REQUEST_METHOD'] == 'POST':
     # put a new html file here!

        output.append("posted things")
        if (form['username'].value != ""):
            use = form['username'].value
 ###### this right here is what's going wrong: I'm getting a KeyError for password
 ###### and I can't figure out why or how to fix it
        if (form['password'].value != ""):
            pw = form['password'].value


#       if (form['username'].value != ""):
#           output.append("username exists")
#       if (form['password'].value != ""):
#           output.append("password exists")
      # if username is correct:
      # print them out (just for now!)
#        output.append(form['username'].value
#        output.append(form['password'].value
      # compare input to the values in username dictionary
#        if form['username'].value in userDict:
      # if it's in the dictionary, compare inputted password to the password in dictionary
#            if form['password'].value == userDict[form['username'].value]:
#                output.append("<p>GREAT SUCCESS")


    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
