from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            c = min(a, b) + cost[i]
            a = b
            b = c

        return min(a, b)


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
