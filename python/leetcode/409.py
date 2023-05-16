class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        bag = set([])

        for a in s:
            if a in bag:
                bag.remove(a)
                ans += 2
            else:
                bag.add(a)

        if bag:
            ans += 1

        return ans


print(Solution().longestPalindrome('abccccdd'))
print(Solution().longestPalindrome('a'))
print(Solution().longestPalindrome('Aa'))
