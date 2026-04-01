class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        seen = set()

        def backTrack(l, start, cur_nums):
            if len(cur_nums) == l and tuple(cur_nums) not in seen:
                res.append(cur_nums[:])
                seen.add(tuple(cur_nums))
                l += 1
            
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                if not cur_nums or nums[i] >= cur_nums[-1]:
                    cur_nums.append(nums[i])
                    backTrack(l, i + 1, cur_nums)
                    cur_nums.pop()
        
        backTrack(2, 0, [])
        return res
            
