class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


for i in range(10):
    print(Solution().climbStairs(i+1))
