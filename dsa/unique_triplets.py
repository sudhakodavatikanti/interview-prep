"""Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0. The solution set must not contain duplicate triplets.

Example: nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]."""

class Solution:
    def three_sum_triplets(self, nums: list[int]) -> list[int]:
        result = []
        sorted_triplet_list = []
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_triplet = sorted([nums[i],nums[j],nums[k]])
                        if sorted_triplet not in sorted_triplet_list:
                            result.append([nums[i],nums[j],nums[k]])
                            sorted_triplet_list.append(sorted_triplet)

                                   

        return result


solution = Solution()
nums = [-1,0, 1, 2, -1, -4]
print(solution.three_sum_triplets(nums))