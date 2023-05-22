class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        P = [[False]*N for _ in range(N)]
        start, end = 0, 0

        for i in range(N):
            P[i][i] = True
            if i > 0:
                P[i-1][i] = s[i-1] == s[i]
                if P[i-1][i] and end-start < 1:
                    start, end = i-1, i

        for i in range(N-3, -1, - 1):
            for j in range(i+2, N):
                P[i][j] = P[i+1][j-1] and s[i] == s[j]
                if P[i][j] and end-start < j-i:
                    start, end = i, j

        return s[start:end+1]


print(Solution().longestPalindrome("saaaaas"))
print(Solution().longestPalindrome("baab"))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("babaabd"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("ddabcdcba"))
print(Solution().longestPalindrome("abbaabba"))
print(Solution().longestPalindrome("abbba"))
