#ifndef SDHGRILL_H
#define SDHGRILL_H

#include <string>
#include <iostream>
using namespace std;
#include <meat.h> 

class SDHgrill {
	public:
		SDHgrill(Meat meatfood);
		void showInfo();		
	private:
		Meat meatfood;
};

#endif
