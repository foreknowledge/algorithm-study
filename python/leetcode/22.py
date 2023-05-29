from typing import *


class Solution:
    # (solution) DP
    def generateParenthesis(self, n: int) -> List[str]:
        F = [[""]]

        for i in range(1, n+1):
            f = []
            for j in range(i):
                f.extend(["(" + a + ")" + b for a in F[i-1-j] for b in F[j]])
            F.append(f)

        return F[-1]


print(Solution().generateParenthesis(3))
