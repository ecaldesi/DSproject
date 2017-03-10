#!/usr/bin/env python2.7
import string

pageTemplate= '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Meal Planner App </title>
  <h1>Welcome to our meal planner application!</h1>
</head>
<body>

<h2>Lets have some {mealtime}!</h2>
<p>Put some mealtime specific greeting here </p>

<h2>Protein </h2>
<p>Dish: to be spit out from input -- {meat} </p>
<p>Calories: to be determined </p>

<h2>Side 1 </h2>
<p>Dish: {veggies} </p>
<p>Calories: to be determined </p>

<h2>Side 2 </h2>
<p>Dish: {fruit} </p>
<p>Calories: to be determined </p>

<h2>Drink </h2>
<p>Dish: {drink} </p>
<p>Calories: to be determined </p>

<h2>Results </h2>
<p>Dishes: {meat}, {fruit}, {veggies}, and a {drink} </p>
<p>Calories: too many </p>




</body>
</html>
'''
   
def main():
    #VARIABLES TO BE USED IN FUNCTIONS
    mealtime = raw_input("Enter breakfast, lunch, or dinner: ")
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
