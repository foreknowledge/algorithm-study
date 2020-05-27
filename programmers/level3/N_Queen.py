def promising(board, x, y):
    n = len(board)
    for i in range(1, y+1):
        if board[x][y-i] != 0: return False
        if x-i >= 0 and board[x-i][y-i] != 0: return False
        if x+i < n and board[x+i][y-i] != 0: return False

    return True

def nqueen(n, board, col):
    if col == n: return 1
    
    result = 0
    for i in range(n):
        if promising(board, i, col):
            board[i][col] = 1
            result += nqueen(n, board, col+1)
            board[i][col] = 0
    
    return result

def solution(n):
    board = [[0]*n for _ in range(n)]
    return nqueen(n, board, 0)

if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    # print(solution(12))       # 시간 초과...