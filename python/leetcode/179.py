from typing import *


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ordered = []

        for n in nums:
            str_n = str(n)
            i = 0
            for o in ordered:
                if str_n + o > o + str_n:
                    break
                i += 1

            ordered.insert(i, str_n)

        return '0' if ordered[0] == '0' else ''.join(ordered)


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution2:
    # sort를 이용한 버전
    def largestNumber(self, nums: List[int]) -> str:
        largest = ''.join(
            sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest[0] == '0' else largest


print(Solution2().largestNumber([10, 2]))
print(Solution2().largestNumber([3, 30, 34, 5, 9]))
print(Solution2().largestNumber([9, 5, 34, 30, 3]))
print(Solution2().largestNumber([10, 2, 9, 39, 17]))
print(Solution2().largestNumber([0, 0]))
print(Solution2().largestNumber([0, 0, 0, 3, 3, 0, 0, 0]))
