from typing import *
from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf

        partial_max = -inf
        for n in nums:
            partial_max = max(partial_max + n, n)
            ans = max(ans, partial_max)

        return ans


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
