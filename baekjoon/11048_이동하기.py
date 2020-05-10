def solution(n,m,maze):
    candy = [[0]*m for _ in range(n)]
    candy[0][0] = maze[0][0]
    for i in range(1,n):
        candy[i][0] = candy[i-1][0]+maze[i][0]
    for j in range(1,m):
        candy[0][j] = candy[0][j-1]+maze[0][j]

    for i in range(1,n):
        for j in range(1,m):
            if i>1 and j>1:
                candy[i][j] = max(candy[i-1][j-1], candy[i][j-1], candy[i-1][j]) + maze[i][j]

    print(candy)


if __name__ == "__main__":
    n,m = map(int, input().split())
    maze = [list(map(int, list(input().split()))) for _ in range(n)]

    solution(n,m,maze)