class Solution:
    def isHappy(self, n: int) -> bool:
        seen =set()

        while n not in seen:
            seen.add(n)
            sumOfdigitSqr=0


            for digit in str(n):
                sumOfdigitSqr += pow(int(digit),2)

            n=sumOfdigitSqr
            if sumOfdigitSqr == 1:
                return True
               

        return n == 1
