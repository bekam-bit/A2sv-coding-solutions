class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_counter=Counter(nums)
        return False if all(nums_counter[num] == 1 for num in nums) else True
