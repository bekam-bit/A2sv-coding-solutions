class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mxi = [0] * n
        prefix_gcd = [0] * n

        for i in range(n):
            if i == 0:
                mxi[i] = nums[i]
                prefix_gcd[i] = nums[i]
            
            else:
                mxi[i]  = max(mxi[i - 1], nums[i])
                prefix_gcd[i] = gcd(mxi[i], nums[i])

        prefix_gcd.sort()

        sumGcdVal = 0
        start = 0
        end = len(prefix_gcd) - 1

        while start < end:
            sumGcdVal += gcd(prefix_gcd[start], prefix_gcd[end])
            start += 1
            end -= 1
        
        return sumGcdVal