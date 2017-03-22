nclude <iostream>
#include <string>
#include "meat.h"
#include "chicken.h"

using namespace std;

Chicken::Chicken (string NameVal, string CaloriesVal) : Meat (NameVal, CaloriesVal) {}

void Chicken::print() {
	cout << "Type of chicken: " << getName() << endl;
	cout << "Calories: " << getCalories() << endl;
}
