class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        nums_idx={}

        for idx, num in enumerate(sorted_nums):
            if num not in nums_idx:
                nums_idx[num] = idx

        res=[]
        for num in nums:
            res.append(nums_idx[num])

        return res
