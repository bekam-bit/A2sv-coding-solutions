class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)

        perimeter=0
        for i in range(len(nums)-2):
            if sorted_nums[i] + sorted_nums[i+1] > sorted_nums[i+2]:
                perimeter = sum(sorted_nums[i:i+3])
        
        return perimeter

            
