def solution(triangle):
    answer = [triangle[0]]
    
    for i in range(1, len(triangle)):
        layer = [answer[i-1][0]+triangle[i][0]]
        last_index = len(triangle[i])-1
        for j in range(1, last_index):
            layer.append(max(answer[i-1][j-1],answer[i-1][j])+triangle[i][j])
        layer.append(answer[i-1][last_index-1]+triangle[i][last_index])
        answer.append(layer)
    
    return max(answer[len(triangle)-1])

if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
