from typing import *


class Solution:
    def findAscIdx(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                return i-1
        return -1

    def nextPermutation(self, nums: List[int]) -> None:
        i = self.findAscIdx(nums)
        if i < 0:
            nums.reverse()
            return nums

        subList = sorted(nums[i+1:])
        for j in range(len(subList)):
            nums[i+1+j] = subList[j]

        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                break

        return nums


class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)

        # Find the largest index k such that nums[k] < nums[k + 1].
        k = -1
        for i in range(N-1, 0, -1):
            if nums[i-1] < nums[i]:
                k = i-1
                break

        # If no such index exists, the permutation is the last permutation.
        if k < 0:
            nums.reverse()
            return nums

        # Find the largest index l such that nums[l] > nums[k].
        l = -1
        for i in range(N-1, k, -1):
            if nums[k] < nums[i]:
                l = i
                break

        # swap nums[k] with nums[l].
        nums[k], nums[l] = nums[l], nums[k]

        # Reverse the sequence from k+1 to N-1.
        nums[k+1:] = nums[N-1:k:-1]

        return nums


print(Solution2().nextPermutation([1, 2, 3]))
print(Solution2().nextPermutation([3, 2, 1]))
print(Solution2().nextPermutation([1, 1, 5]))
print(Solution2().nextPermutation([1, 3, 2]))
print(Solution2().nextPermutation([3, 4, 2, 1]))
print(Solution2().nextPermutation([1, 3, 4, 5, 3, 2, 1]))
