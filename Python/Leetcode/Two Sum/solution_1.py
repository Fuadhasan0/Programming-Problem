# minimum Memory complexity
class Solution:
       def twoSum(self, nums, target):
              for i in range(len(nums)):
                     for j in range(i + 1, len(nums)):
                            if nums[i] + nums[j] == target:
                                   return [i, j]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Indices: {result}")
