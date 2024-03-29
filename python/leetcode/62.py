class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0] * n for _ in range(m)]
        for i in range(m):
            board[i][0] = 1
        for j in range(n):
            board[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]

        return board[-1][-1]


print(Solution().uniquePaths(3, 7))
print(Solution().uniquePaths(3, 2))
