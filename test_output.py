#!/usr/bin/env python2.7
import string

pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html style="background-color:lightblue">
<head>
<meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
<title>Book Feed </title>
<h1 style="color:black">Welcome to your source for information!</h1>
</head>
<body style="background-color:lightblue">

<h2 style="color:blue" href="https://www.google.com> Trending in Politics ... </h2>
<p style="color:green"> Find out what's trending YOUR world! </p>


<a href="PoliticsSub.html"> /r/politics</a><br>
<a href="WorldnewsSub.html"> /r/worldnews</a><br>
<a href="TechnologySub.html"> /r/technology</a><br>
<a href="FuturologySub.html"> /r/Futurology</a><br>
<a href="ScienceSub.html"> /r/science</a><br>
<a href="SportsSub.html"> /r/sports</a><br>
<a href="BooksSub.html"> /r/Books</a><br>
<a href="CustomSub.html"> /r/Memes</a><br>
</form> 
</body>
</html>
'''
   
def main():
    #VARIABLES TO BE USED IN FUNCTIONS
    contents = pageTemplate.format(**locals())
    browseLocal(contents)
 
def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))                                   

main()
