from typing import *
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        N = len(target)
        for i in range(N // 2):
            if target[i] == target[N-1-i]:
                continue
            return False

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
