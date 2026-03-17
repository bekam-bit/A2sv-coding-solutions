class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1/x
            n = -n
        
        if n == 1:
            return x
        
        return x * self.pow(x, n - 1)

    def pow(self, base, exp):
        if exp == 0:
            return 1.0
        
        half = self.pow(base, exp//2)
        
        if exp % 2 == 0:
            return half * half

        else:
            return half * half * base
    
        
        
