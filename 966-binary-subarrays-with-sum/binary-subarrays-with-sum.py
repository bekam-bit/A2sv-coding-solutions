class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        cur_sum = 0
        freq = Counter()
        freq[0] = 1
        total_cnt = 0

        for i in range(n):
            cur_sum += nums[i]

            if cur_sum - goal in freq:
                total_cnt += freq[cur_sum - goal]

            freq[cur_sum] += 1

        return total_cnt
            

