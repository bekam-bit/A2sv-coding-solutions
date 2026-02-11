class Solution:
    def romanToInt(self, s: str) -> int:
        s_v_pair = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        integer=0
        prev=0

        for i in range(len(s)-1,-1,-1):
            cur = s_v_pair[s[i]]
            if cur < prev:
                integer -= cur
            else:
                integer += cur
            
            prev=cur
        
        return integer
                    
