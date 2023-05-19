from typing import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            r = [1]
            for j in range(1, i):
                r.append(row[j-1] + row[j])
            r.append(1)
            row = r
        return row


class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(1, rowIndex+1):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


for i in range(0, 10):
    print(Solution().getRow(i))
    print(Solution2().getRow(i))
