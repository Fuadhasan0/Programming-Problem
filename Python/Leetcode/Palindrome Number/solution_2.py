class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Special case for numbers ending in 0, but not 0 itself
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_num = 0
        original = x
        
        while x > 0:
            # Add the last digit to reversed_num
            reversed_num = reversed_num * 10 + x % 10
            # Remove the last digit from x
            x //= 10
        
        # Check if the original number is the same as the reversed number
        return original == reversed_num
