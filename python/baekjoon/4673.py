# 4673. 셀프 넘버


def d(n):
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result


def solution():
    MAX_NUM = 10001
    nums = [0 for _ in range(MAX_NUM)]

    for i in range(1, MAX_NUM):
        n = d(i)
        if n < MAX_NUM:
            nums[n] = 1

        if nums[i] == 0:
            print(i)


solution()
