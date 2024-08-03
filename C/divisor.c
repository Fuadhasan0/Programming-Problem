/*
Problem is ~

   Firstly, input who much number run this code. And then print single line for single number and whole number who divisor for this number.


*/

#include<stdio.h>

int main(){
       int T, N, i, j;

       scanf("%d", &T);

       for( i=1; i<=T; i++){

              scanf("%d", &N);
              printf("Case %d:", i);

              for(j=1; j<=N; j++){
                     if(N%j == 0){
                     printf(" %d", j);
              }

              }
              printf("\n");
       }

       return 0;
}