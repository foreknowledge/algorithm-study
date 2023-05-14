from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        s, e = 0, len(height)-1

        while s < e:
            area = max(area, (e-s)*min(height[s], height[e]))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
