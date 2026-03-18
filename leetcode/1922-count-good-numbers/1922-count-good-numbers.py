class Solution:
    MOD = pow(10,9) + 7

    def countGoodNumbers(self, n: int) -> int:
        length = 0

        evens = (n + 1) // 2
        odds = n // 2

        length = (self.sqr(5, evens) * self.sqr(4, odds)) % self.MOD

        return length
        
    def sqr(self, base:int, exp:int) -> int:

        if exp == 0:
            return 1

        half = self.sqr(base, exp // 2)

        res = (half * half) % self.MOD

        if exp % 2 != 0:
            res = (res * base) % self.MOD
        
        return res
        
        

     
        