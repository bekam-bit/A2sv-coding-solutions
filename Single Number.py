class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_nums=Counter(nums)
        for i in range(len(nums)):
            if cnt_nums[nums[i]] != 2:
                return nums[i]

               
               
