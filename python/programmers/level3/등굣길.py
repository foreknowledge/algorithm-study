def solution(m, n, puddles):
    roads = [[1]*m for _ in range(n)]

    for p in puddles:
        roads[p[1]-1][p[0]-1] = 0

    # 1열 채우기
    for i in range(1, n):
        if roads[i-1][0] == 0:
            roads[i][0] = 0

    # 1행 채우기
    for j in range(1, m):
        if roads[0][j-1] == 0:
            roads[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if roads[i][j] == 1:
                roads[i][j] = (roads[i-1][j] + roads[i][j-1]) % 1000000007

    return roads[n-1][m-1]

if __name__ == "__main__":
    print(solution(4,3,[[2,2]]))
