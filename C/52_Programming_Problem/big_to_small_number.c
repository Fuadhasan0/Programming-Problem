/*
Problem is~
    
    Firstly, input who much number run this code. And then print number 1000 to 1 and 5 number in 1 line with single tap gap between two number
*/

#include<stdio.h>

int main(){

       for(int i=1000; i>0; i--){
              if(i%5 == 0){
                     printf("\n");
              }
              printf("%d\t", i);
       }

       return 0;
}