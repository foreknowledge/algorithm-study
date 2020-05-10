def solution(heights):
    answer = []

    for i in range(len(heights)-1, -1, -1):
        exist = False
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]: 
                answer.append(j+1)
                exist = True
                break
        if not exist: answer.append(0)

    answer.reverse()

    return answer


if __name__ == "__main__":
    print(solution([6,9,5,7,4]))
    print(solution([3,9,9,3,5,7,2]))
    print(solution([1,5,3,6,7,6,5]))