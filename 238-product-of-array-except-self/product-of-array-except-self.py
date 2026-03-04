class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans  = [1] * n

        left = 1
        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]

        right = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= right
            right *= nums[j]
        
        return ans