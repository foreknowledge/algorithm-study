# 14500 테트로미노

tetrominoes = [
    # I
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],
    # O
    [[1, 1], [1, 1]],
    # L
    [[1, 0], [1, 0], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1], [0, 1], [0, 1]],
    [[0, 0, 1], [1, 1, 1]],
    # J
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[1, 1], [1, 0], [1, 0]],
    [[1, 1, 1], [0, 0, 1]],
    # S
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1, 1], [1, 1, 0]],
    # Z
    [[0, 1], [1, 1], [1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    # T
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1], [1, 1], [0, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0], [1, 1], [1, 0]],
]


def findSum(maze, tetromino, iOffset, jOffset):
    sum = 0
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] == 1:
                sum += maze[iOffset + i][jOffset + j]
    return sum


def solution():
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]

    max = 0

    for tetromino in tetrominoes:
        tn = len(tetromino)
        tm = len(tetromino[0])
        for iOffset in range(0, n - tn + 1):
            for jOffset in range(0, m - tm + 1):
                sum = findSum(maze, tetromino, iOffset, jOffset)
                if max < sum:
                    max = sum

    return print(max)


solution()
