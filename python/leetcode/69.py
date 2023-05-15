class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2
            sqr = mid*mid
            if sqr == x:
                return mid
            if sqr < x:
                l = mid+1
            else:
                r = mid-1

        return l-1


print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(10))
print(Solution().mySqrt(16))
