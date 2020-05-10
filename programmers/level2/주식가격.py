def solution(prices):
    answer = []
    for i in range(len(prices)):
        ans = 0
        t = prices[i]
        for j in range(i+1,len(prices)):
            ans += 1
            if (t <= prices[j]): continue
            else: break
        answer.append(ans)
        
    return answer


if __name__ == "__main__":
    print(solution([3,4,5,2,1,6,2,4,3,1]))
    print(solution([3,4,3,2,5,6,1,2]))