#include<stdio.h>
#include<stdbool.h>

bool isPalindrome(int x) {
    if (x < 0) return false;  // Negative numbers are not palindromes

    long long temp = 0;
    long long c = 0;
    long long original = x;

    while (x > 0) {
        c = x % 10;
        x /= 10;
        temp = temp * 10 + c;
    }

    return temp == original;
}