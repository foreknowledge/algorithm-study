from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                pivot = i
                break

        l, r = 0, len(nums)-1
        if pivot == 0 or nums[0] > target:
            l = pivot
        else:
            r = pivot

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1

        return False


class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            while l < len(nums)-1 and nums[l] == nums[l+1]:
                l += 1
            while r > 0 and nums[r] == nums[r-1]:
                r -= 1

            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return False


print(Solution2().search([2, 5, 6, 0, 0, 1, 2], 0))
print(Solution2().search([2, 5, 6, 0, 0, 1, 2], 3))
print(Solution2().search([0, 0, 1, 2, 3, 5, 7], 3))
print(Solution2().search([2, 2, 2, 3, 2, 2, 2], 3))
print(Solution2().search([1], 1))
print(Solution2().search([1, 2, 1, 1, 1], 2))
