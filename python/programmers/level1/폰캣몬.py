from typing import *


def solution(nums: List[int]):
    return min(len(set(nums)), len(nums) // 2)


print(solution([1, 2, 3, 3, 1, 2, 3, 3]))
