#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int roll_dice(void);
bool play_game(void);

/* roll_dice function */
int roll_dice(void)
{
  int dice1,dice2,dice_sum;
	dice1 = (rand() % 6) + 1; //+1 to eliminate 0
  dice2 = (rand() % 6) + 1;
	dice_sum = dice1 + dice2;
	return dice_sum;
}

/* play game function */
bool play_game(void)
{
	bool win = false,repeat = true;
	int point = 0; 		  
  int roll_sum = 0;
	roll_sum = roll_dice();
  printf("\nYou rolled: %d\n", roll_sum);
  if (roll_sum == 7 || roll_sum == 11){
    win = true;
    printf("You win!\n");
  }
  else if (roll_sum == 2 || roll_sum == 3 || roll_sum == 12){
    win = false;
    printf("You lose!\n");
  }
  else{
    point = roll_sum;
  }


	if (point > 0) {
		printf("Your point is %d\n", point);
		while (repeat == true){
			int roll_sum = 0;
      roll_sum = roll_dice();
      printf("You rolled: %d\n", roll_sum);
			if (roll_sum == 7) {
				repeat = false;
				win = false;
				printf("You lose!\n");
			}
			if (roll_sum == point) {
				repeat = false;
				win = true;
        printf("You win!\n");
			}
		} 
	}
	return win;
}

/* main function */
int main(void)
{
	int wins = 0,losses = 0;
	bool Continue = true;
  char play;

  srand(time(0));  //current time as seed for random generator

  /* loop for play_game */
	while (Continue) {
    if (play_game()){
      wins++;
    }
    else{
      losses++;
    }
		printf("\nPlay again? (y/n): ");
    scanf(" %c", &play);
    if (play == 'Y' || play == 'y'){
      Continue = true;
    }
    else{
      Continue = false;
    }
	}
	printf("\nWins: %d  Losses: %d\n", wins, losses);

	return 0;
}
