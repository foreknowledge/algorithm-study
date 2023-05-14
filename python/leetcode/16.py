
from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 100000

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s

                if abs(ans-target) > abs(s-target):
                    ans = s

                if s < target:
                    j += 1
                else:
                    k -= 1

        return ans


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest([-1, 2, 0, 1, -4], 1))
print(Solution().threeSumClosest([0, 0, 0], 1))
print(Solution().threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
