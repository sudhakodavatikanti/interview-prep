"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operator.

Example: nums = [1,2,3,4] → answer = [24,12,8,6]."""

class Solution:
    def find_array_product(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


solution = Solution()
print(solution.find_array_product([1, 2, 3, 4]))  # [24, 12, 8, 6]

