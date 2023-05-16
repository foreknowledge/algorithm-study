from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The starting range of the first jump is [0, 0]
        ans = 0
        end, far = 0, 0

        for i in range(len(nums)-1):
            # Update the farthest reachable index of this jump.
            far = max(far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == end:
                ans += 1
                end = far

        return ans


print(Solution().canJump([2, 3, 1, 4, 1]))
print(Solution().canJump([2, 3, 0, 1, 4]))
print(Solution().canJump([1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution().canJump([1]))
print(Solution().canJump([1, 2]))
print(Solution().canJump([1, 2, 3]))
print(Solution().canJump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
