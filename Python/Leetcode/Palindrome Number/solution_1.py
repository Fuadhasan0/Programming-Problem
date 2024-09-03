class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the integer to a string to compare the reversed version
        str_x = str(x)
        return str_x == str_x[::-1]
