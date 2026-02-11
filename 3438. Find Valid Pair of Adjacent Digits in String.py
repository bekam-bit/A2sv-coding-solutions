class Solution:
    def findValidPair(self, s: str) -> str:
        s_cnt=Counter(s)

        res=[]

        for i in range(len(s)-1):
            if s[i] != s[i+1] and s_cnt[s[i]] == int(s[i]) and s_cnt[s[i+1]] == int(s[i+1]) and s[i] not in res and s[i+1] not in res:
                res.extend([s[i],s[i+1]])
                return "".join(res) 
        return ""
       
       
        
