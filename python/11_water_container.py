class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        m = min(height[l], height[r]) * r
        while l != r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            m = max(min(height[l], height[r]) * (r - l), m)
        return m
