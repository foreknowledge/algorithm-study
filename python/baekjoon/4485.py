from collections import deque

# Dijkstra 알고리즘
# (0,0)에서 시작해 BFS를 돌면서 루피를 더 적게 먹는 방향으로 나아간다.
cnt = 0
INF = 1e9
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break

    cave = [list(map(int, input().split())) for i in range(n)]
    theif = [[INF for _ in range(n)] for _ in range(n)]

    theif[0][0] = cave[0][0]
    q = deque()
    q.append((0, 0))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if theif[x][y] + cave[nx][ny] < theif[nx][ny]:
                    theif[nx][ny] = theif[x][y] + cave[nx][ny]
                    q.append((nx, ny))

    print('Problem {i}: {ans}'.format(i=cnt, ans=theif[n-1][n-1]))
