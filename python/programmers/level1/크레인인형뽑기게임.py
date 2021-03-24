def solution(board, moves):
        basket = []
        answer = 0

        for i in moves:
            answer += putAndErase(basket, popItem(board, i-1))

        return answer

def popItem(board, col):
    i = 0

    while i < len(board[0]):
        item = board[i][col]
        if item != 0:
            board[i][col] = 0
            return item
        i += 1

    return None

def putAndErase(basket, item):
    if item != None:
        if len(basket) != 0 and basket[-1] == item:
            basket.pop()
            return 2
        basket.append(item)

    return 0

if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))