class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(n:int)-> int:
            cur_cnt = 0
            left = 0
            cnt = Counter()
            total_cnt = 0
            
            for right in range(len(nums)):
                cnt[nums[right]] += 1

                while left < len(nums) and len(cnt) > n:
                    cnt[nums[left]] -= 1

                    if cnt[nums[left]] == 0:
                        del cnt[nums[left]]
                    
                    left += 1
                
                cur_cnt = right - left + 1
                total_cnt += cur_cnt
                
            return total_cnt
        
        return atMost(k) - atMost(k-1)