class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cur_cnt = 0
        left = 0
        left2 = 0
        cnt = Counter()
        cnt2 = Counter()
        total_cnt1 = 0
        total_cnt2 = 0

        for right in range(len(nums)):
            cnt[nums[right]] += 1
            cnt2[nums[right]] += 1

            while len(cnt) > k:
                cnt[nums[left]] -= 1

                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                
                left += 1
            
            while len(cnt2) > k - 1:
                cnt2[nums[left2]] -= 1

                if cnt2[nums[left2]] == 0:
                    del cnt2[nums[left2]]
                
                left2 += 1
            
            cur_cnt = right - left + 1
            total_cnt1 += cur_cnt
            
            cur_cnt = right - left2 + 1
            total_cnt2 += cur_cnt
            
        return total_cnt1 - total_cnt2
        
        