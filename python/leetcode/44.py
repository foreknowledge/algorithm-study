class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        s, p, match, starIdx = 0, 0, 0, -1
        while s < len(string):
            # advancing both pointers
            if p < len(pattern) and (pattern[p] == '?' or string[s] == pattern[p]):
                s += 1
                p += 1
            # * found, only advancing pattern pointer
            elif p < len(pattern) and pattern[p] == '*':
                starIdx = p
                match = s
                p += 1
            # last pattern pointer was *, advancing string pointer
            elif starIdx != -1:
                p = starIdx + 1
                match += 1
                s = match
            # current pattern pointer is not *, last pattern pointer was not *
            # characters do not match
            else:
                return False

        # check for remaining charactoers in pattern
        while p < len(pattern) and pattern[p] == '*':
            p += 1

        return p == len(pattern)


print(Solution().isMatch('aa', 'a'))
print(Solution().isMatch('aa', '*'))
print(Solution().isMatch('cb', '?a'))
print(Solution().isMatch('abcdb', 'a*b'))
print(Solution().isMatch('abcda', 'a*b'))
print(Solution().isMatch('abcdab', 'ab*ab'))
print(Solution().isMatch('abcdcb', 'ab*ab'))
