class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
           
       # nums: list[int] ->> nums is a list of integer
       # target: int ->> target is same
       # -> list[int] ->> return type hint
       
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Indices: {result}")

