#include <stdio.h>
//functions
void create_magic_square(int n,int magic_square[n][n]);
void print_magic_square(int n,int magic_square[n][n]);

//function to create the magic square
void create_magic_square(int n,int magic_square[n][n]){
  int row_number = 0, column_number = 0;	//variable declaration
	row_number = 0;
	column_number = n / 2;

  for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {   //padding the square with 0s
			magic_square[i][j] = 0;
		}
	}

  for (int i = 1; i <= n * n; i++) {  //create the magic square
	magic_square[row_number][column_number] = i; //insert the integers to the square
    	int x = 0,y = 0; 
   	x = (row_number - 1);
    	if (x < 0){
      		x = n - 1;
    	}
    	y = (column_number + 1) % n;

    	if (magic_square[x][y] != 0) {
		row_number = (row_number + 1) % n;
		}
		else {
			row_number = x;
			column_number = y;
		}
	}
	print_magic_square(n,magic_square);

}

void print_magic_square(int n,int magic_square[n][n]){
  for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%6d", magic_square[i][j]);
		}
		printf("\n");
	}
}


int main() {
	
  int n;
  int magic_square[n][n];

	printf("This program creates a magic square of a specified size.\nThe size must be an odd number between 1 and 99.\n");
	printf("Enter size of magic square: ");
	scanf("%d", &n);

  create_magic_square(n,magic_square);

	return 0;
}
