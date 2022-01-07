#include <stdio.h>
#include <string.h> 
#include <unistd.h> 
#include <iostream>
#include <algorithm>
#include <array>
#include <cstdlib>

//rotate class used from here: https://stackoverflow.com/questions/40817533/shift-array-elements-in-c-without-loop
template <class Container>
void rotate(Container& container, int n){
	using std::begin;
	using std::end;

	auto new_begin = begin(container);
    std::advance(new_begin, n);

    std::rotate(
        begin(container),
        new_begin,
        end(container)
    );  
}

//I swapped to c to try to get a little more efficiency, and shortly after realized that the age array was fixed and that shifting the array was a solution that required near no computational power.

int main( int argc, char *argv[] ){
	int numDays;
	//std::array<int,300> inputData = {3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3};
	std::array<int, 5> inputData = {3,4,3,1,2};
	if (argc == 2){
		////The toggle doesn't work due to different array size and the fact I have to declare it before the if. I am sure there is a way around, if I were to spend more time on it I would just have it read from file so that other inputs could be added at will. 
		// if(strcmp("provided",argv[2])){
		// 	std::array<int,300> inputData = {3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3};
		// }
		// else{
		// 	std::array<int, 5> inputData = {3,4,3,1,2};
		// }

		numDays = atoi(argv[1]);
		if (numDays == 0){
			printf("Invalid input\nfishApp_(name)[Number of Days to Simulate]\n"); //[test or provided] 
			exit(1);
		}
	}
	else{
		printf("fishApp_(name) [Number of Days to Simulate]\n"); // [test or provided] 
		exit(1);
	}

	std::array<float,9> birthArray = {0,0,0,0,0,0,0,0,0};

	//setup initial birth array using buckets for the number of fish in each cycle
	for(int i = 0; i < (sizeof(inputData)/sizeof(inputData[0])); i++){ 
		//printf("%f ",inputData[i]);
		birthArray[inputData[i]]++;
	}

	//then i only have to loop through the days and do that number of shifts, both of which are very managable equations
	for (int i = 0; i < numDays; i++){
		////prints out the buckets for error checking
		// for(int i = 0; i < (sizeof(birthArray)/sizeof(birthArray[0])); i++){
		// 	printf("%f ",birthArray[i]);
		// }
		// printf("\n");

		rotate(birthArray,1);

		birthArray[6] += birthArray[8];
	
	}

	double total = birthArray[0] + birthArray[1] + birthArray[2] + birthArray[3] + birthArray[4] + birthArray[5] + birthArray[6] + birthArray[7] + birthArray[8];
	printf("days: %d\n",numDays);
	printf("total: %f\n", total);
}