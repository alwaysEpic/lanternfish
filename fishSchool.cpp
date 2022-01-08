#include <stdio.h>
#include <string.h> 
#include <iostream>
#include <algorithm>
#include <array>
#include <cstdlib>
#include <fstream>
#include <vector>


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
	std::vector<int> inputData;
	
	//command line input and parsing
	if (argc == 3){

		std::ifstream inputFile(argv[2]);
		int num;

	    if(!(inputFile)) std::cout<<"error: file could not be read.\n";
	    
	    while(inputFile >> num) {
	        inputData.push_back(num);
	        inputFile.ignore();
	    }
	    
		numDays = atoi(argv[1]);
		if (numDays == 0){
			printf("Invalid input\nfishApp [Number of Days to Simulate] [filename]\n"); 
			exit(1);
		}
	}
	else{
		printf("fishApp [Number of Days to Simulate] [filename]\n");
		exit(1);
	}

	//creating birth array and converting the input data into the buckets
	std::array<float,9> birthArray = {0,0,0,0,0,0,0,0,0};

	//setup initial birth array using buckets for the number of fish in each cycle
	for(int i=0; i < inputData.size(); i++){ 
		//printf("%d ",inputData[i]);
		birthArray[inputData[i]]++;
	}

	//then i only have to loop through the days and do that number of shifts, both of which are very managable equations
	for (int i = 0; i < numDays; i++){
		////prints out the buckets for error checking
		// for(int i = 0; i < (sizeof(birthArray)/sizeof(birthArray[0])); i++){
		// 	printf("%f ",birthArray[i]);
		// }
		// printf("\n");

		//rotates the array left, rolling at position 0
		rotate(birthArray,1);
		//if no fish give birth, then no fish where in bucket 0. If fish are born the fish in bucket zero are then restarted at day 7.
		birthArray[6] += birthArray[8];
	
	}
	//sum the total number of fish
	double total = birthArray[0] + birthArray[1] + birthArray[2] + birthArray[3] + birthArray[4] + birthArray[5] + birthArray[6] + birthArray[7] + birthArray[8];
	printf("days: %d\n",numDays);
	printf("total: %f\n", total);
}