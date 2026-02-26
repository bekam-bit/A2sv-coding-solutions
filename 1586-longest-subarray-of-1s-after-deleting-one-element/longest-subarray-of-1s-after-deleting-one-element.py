class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        zeros_cnt = 0

        cur_len = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_cnt += 1
                  
            while zeros_cnt > 1:
                if nums[left] == 0:
                    zeros_cnt -= 1
                left += 1
            
            cur_len = right - left 
            max_len = max(cur_len, max_len)
            
        return max_len