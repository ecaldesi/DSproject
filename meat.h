// class interface for the class meat, which uses hierarchy to relate to the classes representing the kinds of meat

#ifndef MEAT_H
#define MEAT_H

#include <iostream>
#include <string>
using namespace std;

class Meat {

	public:
		// constructor
		Meat(string = 'empty', string = 'empty');

		// print function
		virtual void print() = 0;

		// accessor functions
		string getName;
		string getCalories;

	private:
		string name;
		string calories;	
};

#endif
