class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
       
        for i in range(n):
            pos = abs(nums[i]) - 1
            
            if nums[pos] < 0:
                res.append(pos + 1) 

            nums[pos] = -(nums[pos])

        return res