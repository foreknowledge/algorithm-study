def bitInvert(a):
    if a == 0: return 1
    elif a == 1: return 0

def decalcomany(before):
    after = []
    for i in range(len(before)-1, -1, -1):
        after.append(bitInvert(before[i]))

    return after

def solution(n):
    answer = [0]

    for _ in range(1, n):
        decal = decalcomany(answer)
        answer.append(0)
        answer.extend(decal)

    return answer

if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))