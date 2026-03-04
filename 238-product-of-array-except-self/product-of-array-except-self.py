class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_pre = [1] * n
        right_pre = [1] * n

        for i in range(len(nums)):
            if i == 0:
                left_pre[i] *= nums[i]
            else:
                left_pre[i] *= left_pre[i-1] * nums[i]
      
        for j in range(len(nums)-1, -1, -1):
            if j == n - 1:
                right_pre[j] *= nums[j]
            else:
                 right_pre[j] *= right_pre[j+1] * nums[j]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right_pre[i+1])
            elif i == n-1:
                res.append(left_pre[i-1])
            else:
                res.append(left_pre[i-1] * right_pre[i+1])
        
        return res