#ifndef CHICKEN_H
#define CHICKEN_H

#include <iostream>
#include <string>
#include "meat.h"

using namespace std;

class Chicken: public Meat {
	public:
		Chicken(string = "empty", string = "empty" , string = "empty");
		// print function
		virtual void print();
};

#endif
