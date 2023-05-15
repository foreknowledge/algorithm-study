class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        t, d = 0, m-1
        while t <= d:
            mid = (t + d) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                t = mid+1
            else:
                d = mid-1

        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[t-1][mid] == target:
                return True
            if matrix[t-1][mid] < target:
                l = mid+1
            else:
                r = mid-1

        return False


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
