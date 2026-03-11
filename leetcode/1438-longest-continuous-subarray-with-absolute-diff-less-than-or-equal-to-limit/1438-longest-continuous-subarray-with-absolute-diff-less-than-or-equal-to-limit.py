class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()

        cur_len = 0
        max_len = 0
        
        left = 0

        for right in range(len(nums)):

            while max_queue and min_queue and abs(max_queue[0] - min_queue[0]) > limit:
                if nums[left] == max_queue[0]:
                   max_queue.popleft()

                if nums[left] == min_queue[0]:
                    min_queue.popleft() 

                left += 1

            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()

            max_queue.append(nums[right])
            
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()

            min_queue.append(nums[right])

            if max_queue and min_queue and abs(max_queue[0] - min_queue[0]) <= limit:
                cur_len = right - left + 1
                max_len = max(cur_len, max_len)
        
        return max_len