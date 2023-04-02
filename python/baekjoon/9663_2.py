# N Queen


# x 번째에 j가 올 수 있는지 확인
def isPromising(row, x, j):
    for i in range(x):
        if row[i] == j or row[i] + (x - i) == j or row[i] - (x - i) == j:
            return False
    row[x] = j
    return True


def queen(row, n, x):
    if x == n:
        return 1

    ans = 0
    for j in range(n):
        if isPromising(row, x, j):
            ans += queen(row, n, x + 1)

    return ans


def solution(n):
    row = [0] * n
    print(queen(row, n, 0))


solution(int(input()))
