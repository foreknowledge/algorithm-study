def nqueen(n, board, col, ld, rd, cl):
    if col == n: return 1
    
    result = 0
    for i in range(n):
        if ld[i-col+n-1] != 1 and rd[i+col] != 1 and cl[i] != 1:
            board[i][col] = 1
            ld[i-col+n-1] = rd[i+col] = cl[i] = 1

            result += nqueen(n, board, col+1, ld, rd, cl)

            board[i][col] = 0
            ld[i-col+n-1] = rd[i+col] = cl[i] = 0
    
    return result

def solution(n):
    board = [[0]*n for _ in range(n)]
    ld = [0]*n*2    # left diagonal
    rd = [0]*n*2    # right diagonal
    cl = [0]*n      # column

    return nqueen(n, board, 0, ld, rd, cl)

if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(12))