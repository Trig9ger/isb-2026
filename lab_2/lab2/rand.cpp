#include <iostream>
#include <fstream>
#include <time.h>


using namespace std;

int main() {
	srand(time(NULL));

	ofstream out;
	
	out.open("cpprand.txt");

	for(int i = 0; i < 128; ++i){
		out << rand()%2;
	}

	out.close();	
}

