from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            if nums1[i] >= nums2[j]:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1

        for k in range(len(res)):
            nums1[k] = res[k]

        return nums1


class Solution2():
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, w = m-1, n-1, m+n-1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1

        return nums1


print(Solution2().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution2().merge([1], 1, [], 0))
print(Solution2().merge([0], 0, [1], 1))
print(Solution2().merge([2, 0], 1, [1], 1))
