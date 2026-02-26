class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        if c == 1 or c == 0:
            return True

        while left <= right:
            if left * left + right * right == c or left * left + left * left == c or right * right + right * right == c :
                return True
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        
        return False
