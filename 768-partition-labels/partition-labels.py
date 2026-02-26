class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {ch:idx for idx, ch in enumerate(s)}

        start = 0
        end = 0
        res = []
        leng = 0

        for i in range(len(s)):
            end = max(end, last_idx[s[i]])

            if i == end:
                leng = end - start + 1
                res.append(leng)
                start = i + 1
        
        return res