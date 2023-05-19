from typing import *


class Solution:
    # self - Time limit exceeded
    def candy(self, ratings: List[int]) -> int:
        candies = [1]

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candies.append(candies[i-1]+1)
            elif ratings[i-1] > ratings[i]:
                candies.append(1)
                if candies[i-1] == 1:
                    for j in range(i-1, -1, -1):
                        if ratings[j] <= ratings[j+1] or candies[j] > candies[j+1]:
                            break
                        candies[j] += 1
            else:
                candies.append(1)

        return sum(candies)


class Solution2:
    # self
    def candy(self, ratings: List[int]) -> int:
        l, min = 0, -1
        val, ans = 1, 1

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                val += 1
                l = i
                min = val
            elif ratings[i-1] == ratings[i]:
                val = 1
                l = i
                min = -1
            elif val > 1:
                val = 1
            else:
                val = 1
                ans += i-l
                if min > 0 and i-l < min:
                    ans -= 1

            ans += val

        return ans


class Solution3:
    def count(self, n) -> int:
        return (n * (n+1)) // 2

    # solution
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)

        candies, up, down, oldSlope = 0, 0, 0, 0
        for i in range(1, len(ratings)):
            newSlope = 1 if ratings[i] > ratings[i -
                                                 1] else -1 if ratings[i] < ratings[i-1] else 0

            if (oldSlope > 0 and newSlope == 0) or (oldSlope < 0 and newSlope >= 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up, down = 0, 0
            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                candies += 1

            oldSlope = newSlope

        candies += self.count(up) + self.count(down) + max(up, down) + 1
        return candies


print(Solution3().candy([1, 0, 2]))
print(Solution3().candy([1, 2, 2]))
print(Solution3().candy([2, 2, 2]))
print(Solution3().candy([3, 2, 1, 2, 2, 2]))
print(Solution3().candy([1, 3, 2, 2, 1]))
print(Solution3().candy([5, 4, 3, 2, 1]))
print(Solution3().candy([1, 3, 4, 5, 2]))
print(Solution3().candy([1, 2, 3, 4, 3, 2]))
print(Solution3().candy([1, 2, 3, 1, 0]))
