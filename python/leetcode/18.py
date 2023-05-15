from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k, l = j+1, len(nums)-1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
        return ans


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2, 2], 8))
