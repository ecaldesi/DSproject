#!/usr/bin/env python2.7


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Meal Planner App </title>
</head>
<body>
Welcome to our meal planner application!
</body>
</html>
'''
   
def main():
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
