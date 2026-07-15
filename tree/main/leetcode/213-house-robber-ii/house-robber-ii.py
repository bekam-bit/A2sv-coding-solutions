class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def dp(nums):
            memo = {}
            m = len(nums)

            def helper(i):
                if i < 0:
                    return 0
                if i == 0:
                    return nums[0]
                if i not in memo:
                    memo[i] = max(helper(i - 1), helper(i - 2) + nums[i])
                return memo[i]

            return helper(m - 1)

        return max(dp(nums[:-1]), dp(nums[1:]))