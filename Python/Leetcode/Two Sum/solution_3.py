# minimum Time complexity
class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the index of each number
        num_map = {}
        for i, num in enumerate(nums):
            # Calculate the complement that would sum up to the target
            complement = target - num
            # If the complement is in the dictionary, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            # Otherwise, add the number and its index to the dictionary
            num_map[num] = i

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [7, 2, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Indices: {result}")
