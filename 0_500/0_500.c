#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define MAX_SIZE 50000

int main()
{
	srand(time(NULL));
	int contain[MAX_SIZE + 1];
	
	// init
	for(int i = 0;i < MAX_SIZE + 1;i ++){
		contain[i] = i;
	}

	int index;
	for(int i = MAX_SIZE;i >= 0;i --){
		index = rand()%(i+1);
		
		printf("%d ", contain[index]);

		if(index != i){
			contain[index] = contain[i];
		}
	}


	return 0;
}
