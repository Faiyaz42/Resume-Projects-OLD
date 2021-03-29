#include <stdio.h>

int main(){
	/*initiating variables */
	int list[4],i,max,min;
	/* user input */
	printf("Enter four integers: ");
	/* put the user integers into an array called list */
	for(i=0;i<=3;i++) {
	scanf ("%d",&list[i]);
	}
	/* max and min initially set to the value of the first element of the array */
	max = list[0];
	min = list[0];

	/* finding the max value using a for loop */
	for (i = 1;i <= 3;i++) {
		if (max < list[i]){
			max = list[i];
		}
	}
	/*finding the min value using a for loop */
	for (i = 1;i <= 3;i++) {
                if (min > list[i]){
                        min = list[i];
                }
        }
	/*output*/
	printf("Largest: %d \n",max);
	printf("Smallest: %d \n",min);
	return 0;
}
