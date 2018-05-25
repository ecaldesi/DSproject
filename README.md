# Data Structures Final Project
**Authors:** Elisabetta Caldesi, Sophie Lancaster, Brianna Hoelting and Anthony DiFalco.

USAGE
----------

Download the API Client library (this was tested on MAC OS) using the following instructions:
- Download pip installer in Terminal using the following command: `sudo easy_install pip`
- Download the Google API client using the following command: `sudo pip install --upgrade google-api-python-client`
- Clone the project repository using the following command: `git clone https://github.com/ecaldesi/DSproject` 
- After successfully cloning the repository make sure the following files are in your folder:
  - script.cpp
  - createHTML.py
  - webLoader.py
  - googleImg.py
  - SDHdinner.txt
  - SDHlunch.txt
  - SDHbreakfast.txt
  - callGoogleImg.py
- Run the Makefile by using the following command: make
- Insert meal preference when prompted using the following input options:
  - B → breakfast
  - L → lunch
  - D → dinner
- Enter food preferences in CSV format when prompted. Ex.) corn,chicken,rice <br />
  NOTE: Make sure there are no spaces in the input <br />
  NOTE: Max of 5 inputs
- Enter total desired calorie count for meal as a single number when prompted. Ex.) 500

If you are running the program on your a local machine, the output will be an HTML page that opens on your preferred browser.<br />

FUTURE PLANS AND IMPLEMENTATIONS
--------------------------------
- implement day-to-day web scraping, which would utilize a Python script to scrape the food items (and their calorie counts) in the dining hall for each meal using the University dining hall websites.
- make the number of menu items on the final HTML output page is dynamic. Right now the page always displays five menu items no matter how many foods are entered.
- implement a similar HTML page for the input. By doing this the Dining Hall Meal Planner would have a more cohesive look and would generally be more user-friendly.
- add filters such as vegetarian, dairy-free, vegan, gluten-free etc.

