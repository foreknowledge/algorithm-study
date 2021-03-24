import queue

def solution(n,m,maze):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    check = [[0]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    q = queue.Queue()
    q.put((0,0))
    check[0][0] = 1
    dist[0][0] = 1

    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m and check[nx][ny] == 0 and maze[nx][ny] == 1:
                q.put((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = 1

    return dist[n-1][m-1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    
    print(solution(n,m,maze))