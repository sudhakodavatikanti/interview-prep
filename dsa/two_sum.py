from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         my_dict =  {}
         for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                return sorted([i, my_dict[complement]])
            else:
                my_dict[nums[i]] = i

solution = Solution()
nums = [2,5, 7, 11]
target = 9
print(solution.twoSum(nums, target))
