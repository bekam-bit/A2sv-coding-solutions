class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ["a", "b", "c"]
        res = []
       
        def backTrack(l, cur_res):
            if len(cur_res) == l:
                res.append(cur_res)
                return
            
            for cur_ch in letters:
                if len(cur_res) > 0 and cur_res[-1] == cur_ch:
                    continue
                
                backTrack(l, cur_res + cur_ch)
        
        backTrack(n, "")

        if len(res) < k:
            return ""
        
        return res[k - 1]


            
            