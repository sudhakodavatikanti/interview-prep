"""Given a list of integers, return True if any value appears at least twice. Otherwise, return False."""
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


solution = Solution()
nums = [1,2,3,4]
print(solution.containsDuplicate(nums))
