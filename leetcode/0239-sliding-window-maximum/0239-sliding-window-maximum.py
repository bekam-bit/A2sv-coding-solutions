class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        
        ans = []
        for right in range(len(nums)):
            while left < right and right - left + 1 > k:
                if nums[left] == queue[0]:
                    queue.popleft()
                left += 1
                
            while queue and queue[-1] < nums[right]:
                queue.pop()
            
            queue.append(nums[right])

            if right - left + 1 == k:
                ans.append(queue[0])
        
        return ans
