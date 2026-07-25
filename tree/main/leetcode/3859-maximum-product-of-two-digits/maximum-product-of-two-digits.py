class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []
        num = n
        while len(str(num)) > 1:
            digit = num % 10
            nums.append(digit)
            num //= 10
        
        nums.append(num)

        if len(str(n)) == 2:
            return nums[0] * nums[1]
        
        nums.sort()
        return nums[-1] * nums[-2]