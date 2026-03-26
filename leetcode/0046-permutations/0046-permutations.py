class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []

        def backTrack(cur_perm):
            if len(cur_perm) == len(nums):
                res.append(cur_perm[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                
                visited.add(nums[i])
                cur_perm.append(nums[i])

                backTrack(cur_perm)

                visited.remove(nums[i])
                cur_perm.pop()
        
        backTrack([])
        return res