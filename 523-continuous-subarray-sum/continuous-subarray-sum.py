class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r = Counter()
        sub_total = 0
        r[0] = -1
 
        for idx, num in enumerate(nums):
            sub_total += num
            rem = sub_total % k

            if rem not in r:
                r[rem] = idx
            elif rem in r and idx - r[rem] >= 2:
                return True
        
        return False