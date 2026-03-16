class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n-1]
        
        op = 0
        for i in range(n - 2, - 1, - 1):
            if nums[i] > last:
                piece = ceil(nums[i] / last)
            
                op += piece - 1

                last = nums[i] // piece
            else:
                last = nums[i]
        
        return op
