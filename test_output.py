#!/usr/bin/env python2.7
import string

pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html style="background-color:powderblue">
<head style="background-color:powderblue">
<meta content="text/html; charset=ISO-8859-1"http-equiv="content-type">
<title>Meal Planner App </title>
<h1 style="color:red">Welcome to our {mealtime} planner application!</h1>
</head>
<body style="background-color:powderblue">

<h2 style="color:blue">Lets get some food!</h2>
<p style="color:green"> {mealtime_message} </p>

<h2 style="color:blue">Protein </h2>
<p style="color:green" >Dish: to be spit out from input -- {meat} </p>
<p style="color:green" >Calories: to be determined </p>

<h2 style="color:blue" >Side 1 </h2>
<p style="color:green" >Dish: {veggies} </p>
<p style="color:green" >Calories: to be determined </p>

<h2 style="color:blue" >Side 2 </h2>
<p style="color:green" >Dish: {fruit} </p>
<p style="color:green" >Calories: to be determined </p>

<h2 style="color:blue" >Drink </h2>
<p style="color:green" >Dish: {drink} </p>
<p style="color:green" >Calories: to be determined </p>

<h2 style="color:blue" >Results </h2>
<p style="color:green" >Dishes: {meat}, {fruit}, {veggies}, and a {drink} </p>
<p style="color:green" >Calories: too many </p>




</body>
</html>
'''
   
def main():
    #VARIABLES TO BE USED IN FUNCTIONS
    mealtime = raw_input("Enter breakfast, lunch, or dinner: ")
    if mealtime[0].lower() == 'b':
        mealtime_message = "Breakfast? Avoid the eggs"
    if mealtime[0].lower() == 'l':
        mealtime_message = "Lunch? The salad is pretty popular"
    if mealtime[0].lower() == 'd':
        mealtime_message = "Dinner? Good luck"
    meat = raw_input("Enter your preferred meat, or 0 for meatless: ")
    ethnic = raw_input("Enter your preferred station, or 0 for any: ")
    veggies = raw_input("Enter your preffered vegetable, or 0 for any: ") 
    fruit = raw_input("Enter your preffered fruit, or 0 for any: ")
    drink = raw_input("Enter a drink if you want to pick your drink (we can match a drink to suite your meal): ")

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
