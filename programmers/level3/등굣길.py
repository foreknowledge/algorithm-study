# -*- coding: utf-8 -*-

def solution(m, n, puddles):
    road = [[-1]*m for _ in range(n)]
    road[0][0] = 1
    
    for puddle in puddles:
        road[puddle[1]-1][puddle[0]-1] = 0

    # 1행 채우기
    for j in range(1, m):
        if road[0][j] == -1:
            road[0][j] = road[0][j-1]

    # 1열 채우기
    for i in range(1, n):
        if road[i][0] == -1:
            road[i][0] = road[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            if road[i][j] == -1:
                road[i][j] = (road[i-1][j] + road[i][j-1])%1000000007

    return road[n-1][m-1]


if __name__ == "__main__":
    print(solution(4,3,[[2,2],[3,2]]))