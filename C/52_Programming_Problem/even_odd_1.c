/*
Problem is ~

       Firstly, input who much number run this code. And then print those number even or odd in a single line.
*/

#include<stdio.h>

int main(){

       int T, n, i;

       scanf("%d", &T);

       for(i=1; i<=T; i++){
              scanf("%d", &n);

              if(n % 2 == 0){
                     printf("even\n");
              }
              else{
                     printf("odd\n");
              }
       }
       return 0;
}