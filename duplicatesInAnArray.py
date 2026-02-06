class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict=Counter(nums)
        res=[]

        for n,cnt in nums_dict.items():
            if cnt>1:
                res.append(n)
        return res
