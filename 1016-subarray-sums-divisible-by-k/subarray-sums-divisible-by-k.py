class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        r = Counter()
        sub_total = 0
        r[0] = 1

        total_cnt = 0
        for idx, num in enumerate(nums):
            
            sub_total += num
            rem = sub_total % k
            total_cnt += r[rem]
            r[rem] += 1

        return total_cnt