class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            pos = abs(nums[i]) - 1
            if nums[pos] < 0:
                return pos + 1
            
            nums[pos] = -(nums[pos])