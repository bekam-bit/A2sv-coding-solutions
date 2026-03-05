class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * n

        min_sum = float('inf')
        for i in range(n):
            if i == 0:
                pre_sum[i] += nums[i]
            else:
                pre_sum[i] = pre_sum[i-1] + nums[i]
            
            min_sum = min(min_sum, pre_sum[i])

        return 1 - min_sum if min_sum < 1 else 1