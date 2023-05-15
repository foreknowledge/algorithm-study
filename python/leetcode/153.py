class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums)-1

        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[l] < nums[mid]:
                l = mid+1
            else:
                r = mid-1


print(Solution().findMin([3, 4, 5, 1, 2]))
print(Solution().findMin([6, 1, 2, 3, 4, 5]))
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin([4, 5, 6, 7, 8, 9, 10, 1, 2]))
print(Solution().findMin([11, 13, 15, 17]))
print(Solution().findMin([8]))
print(Solution().findMin([2, 1]))
print(Solution().findMin([2, 3, 1]))
