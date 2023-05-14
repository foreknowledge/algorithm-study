from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastN = -1000
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == lastN:
                nums.remove(n)
            else:
                i = i + 1
            lastN = n

        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j+1


print(Solution2().removeDuplicates([1, 1, 2]))
print(Solution2().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
