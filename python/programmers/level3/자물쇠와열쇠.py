from typing import *


def fill(field: List[List[int]], key: List[List[int]], rot: int, x: int, y: int):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:
                field[y + i][x + j] += key[i][j]
            elif rot == 1:
                field[y + i][x + j] += key[j][n - 1 - i]
            elif rot == 2:
                field[y + i][x + j] += key[n - 1 - i][n - 1 - j]
            elif rot == 3:
                field[y + i][x + j] += key[n - 1 - j][i]


def check(field: List[List[int]], offset: int, n: int):
    for i in range(n):
        for j in range(n):
            if field[offset + i][offset + j] != 1:
                return False
    return True


def solution(key: List[List[int]], lock: List[List[int]]):
    offset = len(key) - 1
    N = len(lock)

    for y in range(offset + N):
        for x in range(offset + N):
            for rot in range(4):
                field = [[0] * (N + 2 * offset) for _ in range(N + 2 * offset)]
                for i in range(N):
                    for j in range(N):
                        field[offset + i][offset + j] = lock[i][j]
                fill(field, key, rot, x, y)
                if check(field, offset, N):
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
