class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_cnt = Counter(nums)

        sorted_nums = sorted(nums_cnt.items(),key= lambda x : -x[1])
        n = len(nums)
        res = []
       
        for num, cnt in sorted_nums:
            if cnt > n // 3:
                res.append(num)
            else:
                break
        
        return res
    
    
