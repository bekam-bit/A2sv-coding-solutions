class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTrack(idx, cur_res):
            res.append(cur_res[:])

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                cur_res.append(nums[i])
                backTrack(i + 1, cur_res)
                cur_res.pop()
            
        backTrack(0,[])
        return res