class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        tk=celsius+273.15
        tf=celsius*1.80 + 32.00
        res=[]

        res.append(tk)
        res.append(tf)
        return res
