class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre_sum = [0] * n

        for l, r in requests:
            pre_sum[l] += 1
            if r + 1 < n:
              pre_sum[r+1] -= 1 

        for i in range(1,n):
            pre_sum[i] += pre_sum[i-1] 

        perm_nums = [0] * n
        for idx, num in zip(sorted(range(n), key=lambda i:pre_sum[i]), sorted(nums)):
            perm_nums[idx] = num

        total_sum = 0
        for c in range(1, n):
            perm_nums[c] += perm_nums[c-1]

        for l, r in requests:
            total_sum += perm_nums[r] - perm_nums[l-1] if l - 1 > -1 else perm_nums[r]
            
        return total_sum % (pow(10,9) + 7)
                



        
        
