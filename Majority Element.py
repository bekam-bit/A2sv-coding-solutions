class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_cnt=Counter(nums)

        func =lambda num : nums_cnt[num] >  len(nums)//3
        return list(filter(func,nums_cnt))
        
