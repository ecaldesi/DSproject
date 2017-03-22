// Example for a type of meat

#include <iostream>
#include <string>
#include "meat.h"

using namespace std;

// base class pointer
Meat::Meat (string NameVal, string CaloriesVal) {
	Name = NameVal;
	CaloriesVal = CaloriesVal;
}

// print function
void Meat::print() {
	cout << "Meat Name: "<< Name << endl;
	cout << "Meat Calories: " << Calories << endl;
}

string Meat::getName() {
	return Name;
}

string Meat::getCalories() {
	return Calories;
}
