from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            r = [1]
            for j in range(1, i):
                r.append(rows[i-1][j-1] + rows[i-1][j])
            r.append(1)
            rows.append(r)

        return rows


class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            rows.append([x + y for x, y in zip([0]+rows[i-1], rows[i-1]+[0])])
        return rows


print(Solution().generate(5))
print(Solution2().generate(5))
print(Solution().generate(1))
