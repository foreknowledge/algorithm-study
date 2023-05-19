# 시간 초과
def solution(n):
    f = [1, 1, 3, 10]
    if n <= 3:
        return f[n]

    for i in range(4, n+1):
        case = f[i-1] + f[i-2]*2 + f[i-3]*5
        for j in range(i-3):
            mul = 4 if (j+1) % 3 == 0 else 2
            case += f[i-4-j] * mul
        f.append(case % 1000000007)

    return f[n]

# 통과
# f(n) - f(n-3)으로 무한수열 제거


def solution2(n):
    f = [1, 1]

    co1 = [1, 2, 5, 2, 2, 4]
    co2 = [1, 2, 6, 1, 0, -1]
    for i in range(2, n+1):
        val = 0
        if i < 7:
            val = sum(f[i-1-j] * co1[j] for j in range(i))
        else:
            val = sum(f[i-1-j] * co2[j] for j in range(6))
        f.append(val % 1000000007)

    return f[n]


for i in range(1, 11):
    print(solution2(i))
