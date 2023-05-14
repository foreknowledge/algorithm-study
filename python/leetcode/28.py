from typing import *


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            find = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    find = False
                    break
            if find:
                return i

        return -1


print(Solution().strStr('sadbutsad', 'sad'))
print(Solution().strStr('sabutsad', 'sad'))
print(Solution().strStr('leetcode', 'leeto'))
print(Solution().strStr('leetcode', 'code'))
