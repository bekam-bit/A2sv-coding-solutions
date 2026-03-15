class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n 
        right = [n] * n

        stack = []

        for i in range(n):
            while stack and stack[-1][0] > heights[i]:
                right[stack[-1][1]] = i
                stack.pop()
            
            if stack:
                left[i] = stack[-1][1]
                
            stack.append((heights[i],i))
        
        curA = 0
        maxA = 0
        for i in range(n):
            w = right[i] - left[i] - 1 
            h = heights[i]
            curA = w * h
            maxA = max(maxA, curA)
        
        return maxA