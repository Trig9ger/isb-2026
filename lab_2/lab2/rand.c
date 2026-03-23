#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));

    FILE* file = fopen("crand.txt", "w");

	for(int i = 0; i < 128; ++i){
		    fprintf(file, "%d", rand()%2);
	}

	fclose(file);
}