from typing import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        board = [[0] * n for _ in range(m)]
        board[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            board[i][0] = 0 if (obstacleGrid[i][0]) else board[i-1][0]
        for j in range(1, n):
            board[0][j] = 0 if (obstacleGrid[0][j]) else board[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = 0 if (
                    obstacleGrid[i][j]) else board[i-1][j] + board[i][j-1]

        return board[-1][-1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(Solution().uniquePathsWithObstacles(
    [[0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]))
