from typing import *


class Solution:
    # g 기준으로 찾기
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()

        j = 0
        for i in range(len(g)):
            if j >= len(s):
                break
            while j < len(s)-1 and g[i] > s[j]:
                j += 1
            if g[i] <= s[j]:
                j += 1
                ans += 1

        return ans


class Solution2:
    # s 기준으로 찾기
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        for j in range(len(s)):
            if i >= len(g):
                break
            if g[i] <= s[j]:
                i += 1
        return i


print(Solution2().findContentChildren([1, 2, 3], [1, 1]))
print(Solution2().findContentChildren([1, 2], [1, 2, 3]))
print(Solution2().findContentChildren([3, 2, 1, 1], [1, 1]))
print(Solution2().findContentChildren([3, 2, 1], [2, 1]))
print(Solution2().findContentChildren([1, 1, 2, 3], [1, 1, 1, 2, 3]))
