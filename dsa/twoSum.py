"""Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. You may assume each input has exactly one solution, and you may not use the same element twice.

Example: nums = [2,7,11,15], target = 9 → return [0,1]."""

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        my_dict = {}
        for idx in range(0, len(nums)):
            complement = target - nums[idx]
            if complement in my_dict:
                return [my_dict[complement], idx]
            else:
                my_dict[nums[idx]] = idx


solution = Solution()
nums = [2,7, 11, 15]
target = 9
print(solution.two_sum(nums, target))