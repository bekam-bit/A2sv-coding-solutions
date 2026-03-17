class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur_num = 0
        i = 0
        patches = 0

        while cur_num < n:
            if i < len(nums) and nums[i] <= cur_num + 1:
                cur_num += nums[i]
                i += 1
            
            else:
                cur_num += cur_num + 1
                patches += 1
        
        return patches
       