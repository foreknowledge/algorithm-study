from typing import *


class Solution:
    # Brute-force
    def trap(self, height: List[int]) -> int:
        ans = 0

        for i in range(1, len(height)-1):
            leftMax, rightMax = 0, 0
            for j in range(i, -1, -1):
                leftMax = max(leftMax, height[j])
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])
            ans += min(leftMax, rightMax) - height[i]

        return ans


class Solution2:
    # DP
    def trap(self, height: List[int]) -> int:
        ans = 0
        N = len(height)
        leftMax, rightMax = [0]*N, [0]*N
        leftMax[0], rightMax[-1] = height[0], height[-1]
        for i in range(1, N):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(N-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        for i in range(1, N-1):
            ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans


class Solution3:
    # Stack
    def trap(self, height: List[int]) -> int:
        ans = 0
        cur = 0
        st = []

        while cur < len(height):
            while st and height[cur] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                d = cur-st[-1]-1
                h = min(height[cur], height[st[-1]]) - height[top]
                ans += d * h
            st.append(cur)
            cur += 1

        return ans


class Solution4:
    # 2 pointers
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height)-1
        l_m, r_m = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                l_m = max(l_m, height[l])
                ans += max(l_m-height[l], 0)
            else:
                r -= 1
                r_m = max(r_m, height[r])
                ans += max(r_m-height[r], 0)

        return ans


print(Solution4().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution4().trap([4, 2, 0, 3, 2, 5]))
