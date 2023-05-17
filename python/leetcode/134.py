from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, surplus, total_surplus = 0, 0, 0
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i+1

        print(total_surplus, start)
        return -1 if total_surplus < 0 else start


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(Solution().canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))
print(Solution().canCompleteCircuit([2], [2]))
