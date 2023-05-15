from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < target or (lo > 0 and nums[lo] == nums[lo-1]):
                lo += 1
            elif s > target or (hi < len(nums)-1 and nums[hi] == nums[hi+1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1

        return res

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []

        if not nums:
            return res

        average = target // k
        if average < nums[0] or average > nums[-1]:
            return res

        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for subset in self.kSum(nums[i+1:], target-nums[i], k-1):
                res.append([nums[i]] + subset)

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2, 2], 8))
