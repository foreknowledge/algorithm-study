# 날짜 계산


def solution():
    e, s, m = map(int, input().split())
    r = 0
    while True:
        # year % 15 + 1 = e
        # year % 28 + 1 = s
        # year % 19 + 1 = m
        year = 15 * r + e - 1
        if year % 28 + 1 == s and year % 19 + 1 == m:
            print(year + 1)
            return
        r += 1


solution()
