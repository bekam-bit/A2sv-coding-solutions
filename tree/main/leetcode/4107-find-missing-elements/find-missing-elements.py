class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums), max(nums)
        n = len(nums) 

        i = 0
        while i < n:
            correct_idx = nums[i] - min_val
            if correct_idx < n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        cur_nums = set(nums)
        return[num for num in range(min_val, max_val + 1) if num not in cur_nums]
        