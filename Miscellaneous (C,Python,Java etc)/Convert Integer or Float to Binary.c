#include <stdio.h>

int main() {
			//initiate arrays
        int integer,array1[32],array2[32],array3[24],array4[24],m_format[32],exponent[8];
        float floating_point;
        for (int i = 0;i < 32;i++){		//fill the arrays with zero to replace the memory 
                array1[i] = 0;			// preallocated values.
                array2[i] = 0;
                m_format[i] = 0;
        }
        for (int i =0;i < 24;i++){
                array3[i] =0;
                array4[i] = 0;
                if (i <= 7){
                  exponent[i]=0;
                }
        }

	//Integer to binary calculation
        printf("Enter a positive integer: ");
        scanf("%d",&integer);
        int i = 31,rem = 0;		
        while (integer != 0){
                rem = integer%2;	//find the remainder of the integer when divided by 2
                array1[i] = rem;	//insert the remainder value to the array1
                integer = integer/2;	//find the new value by dividing by 2
                i--;			//store the values at the end of the array,first one goes to the last position.
        }
        printf("The machine format is: ");
        for (int i = 0;i < 32;i++){			//print the machine format array1
                printf("%d",array1[i]);
        }
        printf("\n");

        /* Floating point */
        int whole_number = 0,rem2 = 0;		//initiate variables
        float decimal = 0;
        printf("Enter a positive floating point number: ");
        scanf("%f",&floating_point);
        whole_number = floating_point;			//separate the values on left and right of the decimal
        decimal = floating_point - whole_number;
        int i2 = 31;
        while (whole_number != 0){			//find the binary of the whole number,same as above
                rem2 = whole_number%2;
                array2[i2] = rem2;
                whole_number = whole_number/2;
                i2--;
        }

        int r = 0,l = 0;
        r = 31 - i2;		//length of the padding in whole number array
        l = 24 - i2;		//length of the mantissa array  left after whole number fills the matissa array
        int y = 0;
        int p = 0,q=0;
        float b=0,k=0,h=0;
        while (decimal != 0 || y < l) {		//find the binary of the decimal,loop until decimal is zero or the mantissa is filled up
                b = decimal*2;
                q = b;				//store the integer of the multiplied value,i.e the binary value 1 or 0
                array3[p] = q;			//store it in a new array
                if (b >= 1.0){			//if the float value is >= 1.0 then subtract the whole number and take the decimal value and loop again
                        decimal = b - 1.0;
                }
                else if (b < 1.0){		//else if smaller then just store that value and loop again
                        decimal = b;
                }
                p++;				//array3 position increment
        }
        int t = 0,v=0;				
        int j = 32 - r;				
        for (t = 0;t < r;t++){		//store the whole number binary in a new array4,in array2 the values are at the end of the array so we move and store them at the 
          array4[t] = array2[j];	//front of the array4
          j++;
        }
        int c = 0;                   //store the decimal binary array3  by appending it after the whole number binary in array4
        for (v=t;v < 24;v++){
            array4[v] = array3[c];
            c++;
        }
        int count;					//find the first instance of 1 in the joined binary
        for (count=0;count<32;count++){
          if (array4[count] == 1){
              break;
          }
        } 
        int exp = 0;
        count++;
        exp = r - count;			//find the exponent value by subtracting the length of the binary with the first instace of one position in array4
        exp = exp + 127;
        int mantissa[23];			//mantissa array
        for(int count2 = 0;count2 < 23;count2++){	//initiate loop to insert the decimal values to the mantissa array
          if (count < 24){
            mantissa[count2] = array4[count];		//if theres a value in array4,two different counters since array4 is 24 length
            count++;
          }				
          else{
            mantissa[count2] = 0;			//if no values,pad mantissa with zero
          }
        }
        int i3 = 7,rem3=0;				//find the binary of the exponent
        while (exp != 0){
                rem3 = exp%2;
                exponent[i3] = rem3;
                exp = exp/2;
                i3--;
        }
        for (int count = 0;count < 32;count++){		//insert the exponent,mantissa arrays to a new array called m_format
          if (count == 0){
            if (floating_point > 0){			//insert sign
              m_format[0] = 0;
            }
            else{
              m_format[0] = 1;
            }
          }						
          else if (count >= 1 && count <= 8){		//insert exponent array
            m_format[count] = exponent[count-1];
          }
          else{
            m_format[count] = mantissa[count-9];	//insert mantissa array
          }
        }
        printf("The machine format is: ");			//print machine format
        for (int i4 = 0;i4 < 32;i4++){
                printf("%d",m_format[i4]);
        }
	printf("\n");
        return 0;
}
