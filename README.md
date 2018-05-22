# Data Structures Final Project
By Elisabetta Caldesi, Sophie Lancaster, Brianna Hoelting and Anthony DiFalco.

USAGE
----------

Download the API Client library (this was tested on MAC OS) using the following instructions:
- Download pip installer in Terminal using the following command: sudo easy_install pip
- Download the Google API client using the following command: sudo pip install --upgrade google-api-python-client
- Clone our project repository using the following command: git clone https://ecaldesi@gitlab.com/ecaldesi/cse20312.git
- After successfully cloning the repository make sure the following files are in your folder:
  - Script.cpp
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
- implement day-to-day web scraping, which would utilize a Python script to scrape the food items (and their calorie counts) in the dining hall for each meal using the University dining hall websites. This is something that we had hoped to implement at the beginning of the project and tried very hard to accomplish. However, this task became far more complicated than we had originally thought, and we were advised to instead just hard code the information for the purposes of this project. This is a feature that would make the tool we have created more accurate if the user wants to plan a meal for that day. 
- make the number of menu items on the final HTML output page is dynamic. Right now the page always displays five menu items no matter how many foods are entered. While this still works, in order to make the output of the program more precise this would be a good feature to include.
- implement a similar HTML page for the input. By doing this the Dining Hall Meal Planner would have a more cohesive look and would generally be more user-friendly.

