class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        nums_cnt = Counter()
        nums_cnt[0] = 1
        n = len(nums)
        cnt = 0

        for num in nums:
            pre_sum += num
            if pre_sum - k in nums_cnt:
                cnt += nums_cnt[pre_sum - k]
            
            nums_cnt[pre_sum] += 1
        
        return cnt




                