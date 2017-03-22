#include <string>
#include <iostream>
using namespace std;
#include "meat.h"

SDHgrill::SDHgrill(Meat meatfood) : Meatfood(Meatfood){}

void SDHgrill::showInfo(){
	cout << "Meat kind: " << Meatfood.print() << endl;
}
