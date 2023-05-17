
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        for i in range(1, len(prices)):
            tot += max(prices[i] - prices[i-1], 0)

        return tot


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
