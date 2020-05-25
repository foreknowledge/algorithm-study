def solution(n, lost, reserve):
    answer = n - len(lost)
    
    # 도난당한 학생이 여벌의 체육복이 있는 경우
    lost_but_reserve = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            lost_but_reserve.append(l)
            answer += 1

    for n in lost_but_reserve:
        lost.remove(n)

    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
    
    return answer


if __name__ == "__main__":
    print(solution(5, [2,4], [1,3,5]))
    print(solution(5, [2,4], [3]))
    print(solution(6, [1,3,5], [2,4,6]))
    print(solution(5, [1,2], [2,3]))
    print(solution(5, [1,2,3,4,5], [1,2,3,4,5]))