from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
    

solution = Solution()
nums = [-1,0,2,4,6,8]
target = 4
print(solution.binary_search(nums, target))
