class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_idx = {ordr : idx for idx, ordr in enumerate(order)}
        s_cnt = Counter(s)

        n = len(order)

        res = [""] * len(s)

        pos = 0
       
        for st in order:
            if st in s_cnt:
                count = s_cnt[st]
                end = pos + count

                while pos < end:
                    res[pos] = st
                    pos += 1
                
        for st in s:
            if st not in order_idx:
                res[pos] = st
                pos += 1
               
        return "".join(res)
        
        

