# N Queen (시간 초과)


def possibleJ(n, i, queens):
    possibles = [0] * n
    for qi, qj in queens:
        possibles[qj] = 1
        d = i - qi
        if qj + d < n:
            possibles[qj + d] = 1
        if qj - d >= 0:
            possibles[qj - d] = 1

    result = []
    for j in range(len(possibles)):
        if possibles[j] == 0:
            result.append(j)
    return result


def queen(n, i, queens):
    if i == n:
        if len(queens) == n:
            return 1
        else:
            return 0

    sum = 0
    for j in possibleJ(n, i, queens):
        next = queens.copy()
        next.append((i, j))
        sum += queen(n, i + 1, next)
    return sum


def solution(n):
    print(n, queen(n, 0, []))


solution(int(input()))
