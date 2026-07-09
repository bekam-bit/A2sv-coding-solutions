class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        component_id = [0] * n
        cur_id = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cur_id += 1
            
            component_id[i] = cur_id
        
        res = []

        for i in range(len(queries)):
            if component_id[queries[i][0]] == component_id[queries[i][1]]:
                res.append(True)
            else:
                res.append(False)
        
        return res

