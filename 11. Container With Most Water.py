class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        
        minH = float('inf')
        maxA = 0
        while left < right:
            minH = min(height[left], height[right])
            Area = minH * (right - left)
            maxA = max(maxA, Area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maxA
