class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []

        x=int(num/3)
        y=x-1
        z=x+1

        return [y,x,z]
