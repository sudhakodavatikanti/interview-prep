"""Given an array of integers, move all the zeroes to the end of the array in-place, while maintaining the relative order of the non-zero elements. You must do this without making a copy of the array.

For example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]"""

class Solution:
    def move_all_zeroes_to_end(self, nums: list[int])  -> list[int]:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
    
solution = Solution()
nums = [1, 0, 2, 0, 3]
print(solution.move_all_zeroes_to_end(nums))