from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        mark = [0]*N
        mark[-1] = 1

        for i in range(N-2, -1, -1):
            for j in range(i+1, i+1+nums[i]):
                if mark[j] == 1:
                    mark[i] = 1
                    break

        return mark[0] == 1


class Solution2:
    # solution
    def canJump(self, nums: List[int]) -> bool:
        # 가장 멀리 갈 수 있는 위치
        far = 0
        for i, num in enumerate(nums[:-1]):
            far = max(i + num, far)
            if i == far:
                return False
        return True


print(Solution().canJump([2, 3, 1, 0, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))
print(Solution().canJump([1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution().canJump([1, 1, 1, 1, 1, 1, 1, 0, 1]))
