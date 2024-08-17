#include<stdio.h>
#include<string.h>

int main(){
       int T;
       scanf("%d", &T);

       for(int i=0; i<T; i++){
              char number[101];//Since the number can have up to 100 digits
              scanf("%s", number);

              //get the last digit
              int lastDigit = number[strlen(number) - 1] - '0';

              if(lastDigit % 2 == 0){
                     printf("even\n");
              }
              else{
                     printf("odd\n");
              }
       }


       return 0;
}