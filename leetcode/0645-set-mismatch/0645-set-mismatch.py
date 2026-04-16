class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            correct_pos = nums[i] - 1
            if nums[correct_pos] != nums[i]:
                nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]