from typing import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mins = [triangle[0][0]]

        for i in range(1, len(triangle)):
            m = []
            for j in range(i+1):
                if j == 0:
                    m.append(mins[0] + triangle[i][j])
                elif j == i:
                    m.append(mins[j-1] + triangle[i][j])
                else:
                    m.append(min(mins[j-1], mins[j]) + triangle[i][j])
            mins = m

        return min(mins)


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minimumTotal([[-10]]))
