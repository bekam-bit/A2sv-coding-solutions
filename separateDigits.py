class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            num_list=list(str(num))
            for n in num_list:
                res.append(int(n))
        return res
