#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <wiringPi.h>
#include <gertboard.h>
#include <string.h>
#include <iostream>

int main(int argc, char *argv[]) {
	
	wiringPiSetup () ;
	pinMode (0, OUTPUT) ;

	int i, goto_degree;
	
	do {
		std::cin >> goto_degree;
		
		goto_degree = goto_degree*1800/180+600;
		std::cout << goto_degree << "\n";
		
		for(i=0; i<40; ++i){
			delay(20);
			digitalWrite(0, 1);
			delayMicroseconds(goto_degree);
			digitalWrite(0, 0);
		}
	} while(1);
}

// Entre 1.25 et 1.75 ms (0 -> 180)
// 500 a 2000 = 
