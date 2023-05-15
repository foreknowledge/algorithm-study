class Solution(object):
    def findMin(self, nums):
        N = len(nums)
        l, r = 0, N-1

        if N == 1:
            return nums[0]
        if N == 2:
            return min(nums[0], nums[1])
        if nums[l] < nums[r]:
            return nums[0]

        while l <= r:
            while l < N-1 and nums[l] == nums[l+1]:
                l += 1
            while r > 0 and nums[r] == nums[r-1]:
                r -= 1
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[l] < nums[mid]:
                l = mid+1
            else:
                r = mid-1

        return nums[0]


print(Solution().findMin([1, 3, 5]))
print(Solution().findMin([2, 2, 2, 0, 1]))
print(Solution().findMin([2, 2, 2, 2, 2]))
print(Solution().findMin([2, 2, 2, 1, 2]))
print(Solution().findMin(
    [5, 5, 5, 5, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]))
