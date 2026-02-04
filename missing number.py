class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen=set(nums)
        n=len(nums)

        max_num=0
        for i in range(n):
            max_num=max(max_num,nums[i])

        for i in range(max_num+2):
            if i not in seen:
                return i
        
