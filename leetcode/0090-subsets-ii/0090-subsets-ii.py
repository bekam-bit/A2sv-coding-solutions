class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        
        def backTrack(idx, cur_res):
            if tuple(sorted(cur_res)) not in seen:
                res.append(cur_res[:])
                seen.add((tuple(sorted(cur_res))))
                
            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: 
                    continue
                cur_res.append(nums[i])
                backTrack(i + 1, cur_res)
                cur_res.pop()
            
        backTrack(0,[])
        return res