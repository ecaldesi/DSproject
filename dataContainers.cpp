/* below is the bare bones of the data containers for the menu items and nutrition facts of the daily meals at south. They will be populated from a file. */

#ifndef MENU_H
#define MENU_H

#include <iostream>
using namespace std;
#include <string>



struct Menu {
  string location;
  string date;
  string meal;
  vector<item> items;

  Menu(string = "", string = "", string = "");
  ~Menu();
  void add(item);
  void print();

};

struct item {
  string name;
  nutritionFacts info;

  void print();
};

struct nutritionFacts {
  char calories, fat, sodium, carbohydrateTotal, sugar, fiber, protein, servingSize;
};


Menu::Menu(string loc, string dat, string mealN) {
  
  location = loc;
  date = dat;
  meal = mealN;
  

}


#endif
